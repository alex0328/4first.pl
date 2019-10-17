from django.urls import path, re_path
from appforfirst import views



app_name = 'appforfirst'
urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),#v
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),#v
    path('addproject/', views.ProjectCreate.as_view(), name='add_project'),#v
    path('addtask/', views.TasksCreate.as_view(), name='addtask'),#v
    path('adddiary/', views.DiaryCreate.as_view(), name='adddiary'),
    path('addreminder/', views.ReminderCreate.as_view(), name='addreminder'),#v
    path('event/<int:id>', views.Reminder_View.as_view(), name='event'),#v
    path('task/<int:id>', views.Task_View.as_view(), name='task'),#v
    path('diary/<int:id>', views.Diary_View.as_view(), name='diary'),#v
    path('project/<int:id>', views.Project_View.as_view(), name='project'),#v
    path('del_poject/<int:id>', views.DeleteProject_View.as_view(), name='del_project'),#v
    path('success/', views.successView, name='success')#? is needed
]
