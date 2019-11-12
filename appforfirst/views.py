from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View
from appforfirst import models
from django.contrib.auth.models import User
from appforfirst import forms
from datetime import datetime
from django.views.generic.edit \
import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import requests
import json
import feedparser

from django.conf import settings


#index
class MainPageView(View):
    def get(self, request):
        form = ContactForm()
        req = request.META['HTTP_HOST']
        ctx = {
            "form": form,
            "req": req
        }
        return render(request, 'appforfirst/newtemplates/index.html', ctx)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['lukasz.szlaszynski@4tea.pl'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            mess = "Wiadomość została wysłana poprawnie"
            form = ContactForm()
            ctx = {
                "mess": mess,
                "form": form
            }
            return render(request, 'appforfirst/newtemplates/index.html', ctx)


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


#register (in main urls)
class RegisterView(View):
    form_class = forms.UserRegisterForm
    template_name = 'appforfirst/newtemplates/register.html'

    def get(self, request):
        return render(request, 'appforfirst/newtemplates/register.html',
                      {'form': forms.UserRegisterForm()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('/mem')

        return render(request, self.template_name, {'form': form})


#welcome/
class WelcomeView(LoginRequiredMixin, View):
    def get(self, request):
        date = datetime.now()  #raw date
        todays_date = datetime.today() #raw todays date
        weekdayiso = datetime.now().isoweekday() #weekday
        weekdays = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]
        weekday = weekdays[int(weekdayiso-1)] #translation weekday

        #querry for todays events
        all_todays_events = models.Project.objects.filter(Q(diary__diary_data_utworzenia__day=todays_date.day) |
                                                          Q(reminder__reminder_data_wykonania__day=todays_date.day) |
                                                          Q(tasks__task_start_time__day=todays_date.day))


        #query for all projects
        all_for_today_base = models.Project.objects.filter(project_user=request.user)

        #query for todays reminders
        todays_events = models.Reminder.objects.filter(reminder_data_wykonania__year=todays_date.year,
                                                            reminder_data_wykonania__month=todays_date.month,
                                                            reminder_data_wykonania__day=todays_date.day,
                                                            reminder_user=request.user)
        #query for todays tasks
        todays_tasks = models.Tasks.objects.filter(task_start_time__year=todays_date.year,
                                                     task_start_time__month=todays_date.month,
                                                     task_start_time__day=todays_date.day,
                                                     task_user=request.user)
        #query for todays diaries
        todays_diary = models.Diary.objects.filter(diary_data_utworzenia__year=todays_date.year,
                                                     diary_data_utworzenia__month=todays_date.month,
                                                     diary_data_utworzenia__day=todays_date.day,
                                                     diary_user=request.user)

        #lotto and news

        #lotto
        url = 'http://serwis.mobilotto.pl/mapi_v6/index.php?json=getLotto' # lotto api enpoint
        req = requests.get(url).json() #request to api
        num_losowania = req['num_losowania'] #number from reponse
        numerki_tosort1 = req['numerki'] #numbers lotto from response
        numery_order = numerki_tosort1.split(',') #split numbers

        #?
        numerki_tosort = [] #empty list for ordered list
        for i in numery_order:
            if int(i) < 10:
                i = "0" + i
            numerki_tosort.append(i)
        data_losowania_raw = req['data_losowania']
        cut = data_losowania_raw.split(' ')
        data_losowania = cut[0]
        numerki = sorted(numerki_tosort)
        #print(numerki)
        nums = {}
        for idx, val in enumerate(numerki):
            #print(idx, val)
            nums[idx+1] = val
        #print(nums)

        #check in database is allready exist
        rekord_z_data = models.LottoNumbers.objects.filter(draw_date=data_losowania)
        if not rekord_z_data:
            models.LottoNumbers.objects.create(
                draw_date=data_losowania,
                draw_number=num_losowania,
                number_1=numerki[0],
                number_2=numerki[1],
                number_3=numerki[2],
                number_4=numerki[3],
                number_5=numerki[4],
                number_6=numerki[5]
            )
        # print('------------')
        print(request.is_ajax())
        # print()

        #news section
        feeds = feedparser.parse('https://www.tvn24.pl/najnowsze.xml') #news endpoint xml
        news = {}
        for j in feeds.entries:
            news[j.title] = j.links[0]['href']

        ctx = {'news': news,
                'numerki': nums,
                'num_losowania': num_losowania,
                'data_losowania': data_losowania,
                'all_todays_events': all_todays_events,
                'date': date,
                'weekday': weekday,
                'today': all_for_today_base,
                'todays_events': todays_events,
                'todays_tasks': todays_tasks,
                'todays_diary': todays_diary,
               }
        return render(request, 'appforfirst/newtemplates/min_welcome.html', ctx)


#event/<int:id>
class Reminder_View(LoginRequiredMixin, View):
    def get(self, request, id):
        events = models.Reminder.objects.filter(id=id)
        ctx = {'events': events}
        return render(request, 'appforfirst/newtemplates/event.html', ctx)


#task/<int:id>
class Task_View(LoginRequiredMixin, View):
    def get(self, request, id):
        tasks = models.Tasks.objects.filter(id=id)
        ctx = {'tasks': tasks}
        return render(request, 'appforfirst/newtemplates/task.html', ctx)


#diary/<int:id>
class Diary_View(LoginRequiredMixin, View):
    def get(self, request, id):
        diary = models.Diary.objects.filter(id=id)
        ctx = {'diary': diary}
        return render(request, 'appforfirst/newtemplates/diary.html', ctx)


#project/<int:id>
class Project_View(LoginRequiredMixin, View):
    def get(self, request, id):
        project = models.Project.objects.filter(id=id)
        ctx = {'project': project}
        return render(request, 'appforfirst/newtemplates/project.html', ctx)


#addproject/
class ProjectCreate(LoginRequiredMixin, CreateView):
    model = models.Project
    fields = ['project_name','project_description','project_start_date','project_end_date','project_status']
    success_url = reverse_lazy("appforfirst:welcome")

    def form_valid(self, form):
        form.instance.project_user = self.request.user
        return super().form_valid(form)

#addtask/
class TasksCreate(LoginRequiredMixin, CreateView):
    model = models.Tasks
    form_class = forms.TaskForm
    success_url = reverse_lazy("appforfirst:welcome")

    def form_valid(self, form):
        form.instance.task_user = self.request.user
        return super().form_valid(form)


#adddiary/
class DiaryCreate(LoginRequiredMixin, CreateView):
    model = models.Diary
    fields = ['diary_name','diary_description','diary_start_data',
              'diary_end_data', 'diary_wniosek', 'diary_data_powrotu', 'diary_project',
              'diary_custom_field1', 'diary_custom_field2', 'diary_custom_field3', 'diary_custom_field4',
              'diary_custom_field5', 'diary_custom_field6',
              'diary_custom_field7', 'diary_custom_field7', 'diary_custom_field7', 'diary_custom_field10']
    success_url = reverse_lazy("appforfirst:welcome")

    def form_valid(self, form):
        form.instance.diary_user = self.request.user
        return super().form_valid(form)


#addreminder/
class ReminderCreate(LoginRequiredMixin, CreateView):
    model = models.Reminder
    fields = ['reminder_name','reminder_description','reminder_data_wykonania',
              'reminder_is_done', 'reminder_project']
    success_url = reverse_lazy("appforfirst:welcome")

    def form_valid(self, form):
        form.instance.reminder_user = self.request.user
        return super().form_valid(form)


#del_poject/<int:id>
class DeleteProject_View(LoginRequiredMixin, View):
    def get(self, request, id):
        p = models.Project.objects.get(id=id)
        p.delete()
        return render(request, 'appforfirst/newtemplates/del_project_ok.html')






