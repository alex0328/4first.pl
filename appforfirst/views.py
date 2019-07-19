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


class MainPageView(View):
    def get(self, request):
        return render(request, 'appforfirst/newtemplates/index.html')

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

class WelcomeView(LoginRequiredMixin, View):
    def get(self, request):
        date = datetime.now()
        todays_date = datetime.today()
        weekdayiso = datetime.now().isoweekday()
        weekdays = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]
        weekday = weekdays[int(weekdayiso-1)]

        all_todays_events = models.Project.objects.filter(Q(diary__diary_data_utworzenia__day=todays_date.day) |
                                                          Q(reminder__reminder_data_wykonania__day=todays_date.day) |
                                                          Q(tasks__task_start_time__day=todays_date.day))


        all_for_today_base = models.Project.objects.filter(project_user=request.user)

        todays_events = models.Reminder.objects.filter(reminder_data_wykonania__year=todays_date.year,
                                                            reminder_data_wykonania__month=todays_date.month,
                                                            reminder_data_wykonania__day=todays_date.day,
                                                            reminder_user=request.user)

        todays_tasks = models.Tasks.objects.filter(task_start_time__year=todays_date.year,
                                                     task_start_time__month=todays_date.month,
                                                     task_start_time__day=todays_date.day,
                                                     task_user=request.user)

        todays_diary = models.Diary.objects.filter(diary_data_utworzenia__year=todays_date.year,
                                                     diary_data_utworzenia__month=todays_date.month,
                                                     diary_data_utworzenia__day=todays_date.day,
                                                     diary_user=request.user)


        ctx = {'all_todays_events': all_todays_events,
               'date': date,
               'weekday': weekday,
               'today': all_for_today_base,
               'todays_events': todays_events,
               'todays_tasks': todays_tasks,
               'todays_diary': todays_diary,
               }
        return render(request, 'appforfirst/newtemplates/min_welcome.html', ctx)


class WelcomeView2(LoginRequiredMixin, View):
    def get(self, request):
        date = datetime.now()
        todays_date = datetime.today()
        weekdayiso = datetime.now().isoweekday()
        weekdays = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]
        weekday = weekdays[int(weekdayiso-1)]

        all_todays_events = models.Project.objects.filter(Q(diary__diary_data_utworzenia__day=todays_date.day) |
                                                          Q(reminder__reminder_data_wykonania__day=todays_date.day) |
                                                          Q(tasks__task_start_time__day=todays_date.day))




        ctx = {'all_todays_events': all_todays_events,
               'date': date,
               }
        return render(request, 'appforfirst/newtemplates/min_welcome2.html', ctx)

class Reminder_View(LoginRequiredMixin, View):
    def get(self, request, id):
        events = models.Reminder.objects.filter(id=id)
        ctx = {'events': events}
        return render(request, 'appforfirst/newtemplates/event.html', ctx)

class Task_View(LoginRequiredMixin, View):
    def get(self, request, id):
        tasks = models.Tasks.objects.filter(id=id)
        ctx = {'tasks': tasks}
        return render(request, 'appforfirst/newtemplates/task.html', ctx)

class Diary_View(LoginRequiredMixin, View):
    def get(self, request, id):
        diary = models.Diary.objects.filter(id=id)
        ctx = {'diary': diary}
        return render(request, 'appforfirst/newtemplates/diary.html', ctx)

class Project_View(LoginRequiredMixin, View):
    def get(self, request, id):
        project = models.Project.objects.filter(id=id)
        ctx = {'project': project}
        return render(request, 'appforfirst/newtemplates/project.html', ctx)

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = models.Project
    fields = ['project_name','project_description','project_start_date','project_end_date','project_status']
    success_url = reverse_lazy("appforfirst:welcome")

    def form_valid(self, form):
        form.instance.project_user = self.request.user
        return super().form_valid(form)

class ProjectDelete(LoginRequiredMixin, View):
    def get(self, request, project_id):
        pass

class TasksCreate(LoginRequiredMixin, CreateView):
    model = models.Tasks
    form_class = forms.TaskForm
    success_url = reverse_lazy("appforfirst:welcome")

    def form_valid(self, form):
        form.instance.task_user = self.request.user
        return super().form_valid(form)

class Preview(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'appforfirst/newtemplates/min_welcome.html')

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

class ReminderCreate(LoginRequiredMixin, CreateView):
    model = models.Reminder
    fields = ['reminder_name','reminder_description','reminder_data_wykonania',
              'reminder_is_done', 'reminder_project']
    success_url = reverse_lazy("appforfirst:welcome")

    def form_valid(self, form):
        form.instance.reminder_user = self.request.user
        return super().form_valid(form)

class DeleteProject_View(LoginRequiredMixin, View):
    def get(self, request, id):
        p = models.Project.objects.get(id=id)
        p.delete()
        return render(request, 'appforfirst/newtemplates/del_project_ok.html')

