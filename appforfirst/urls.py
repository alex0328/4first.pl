from django.urls import path, re_path
from appforfirst import views



app_name = 'appforfirst'
urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('addproject/', views.ProjectCreate.as_view(), name='add_project'),
    path('addtask/', views.TasksCreate.as_view(), name='addtask'),
    path('adddiary/', views.DiaryCreate.as_view(), name='adddiary'),
    path('addreminder/', views.ReminderCreate.as_view(), name='addreminder'),
    path('event/<int:id>', views.Reminder_View.as_view(), name='event'),
    path('task/<int:id>', views.Task_View.as_view(), name='task'),
    path('diary/<int:id>', views.Diary_View.as_view(), name='diary'),
    path('project/<int:id>', views.Project_View.as_view(), name='project'),
    path('preview', views.Preview.as_view(), name='preview'),
]
