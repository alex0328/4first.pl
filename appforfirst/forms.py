from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from forfirst import models



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Tasks
        fields = ['task_type', 'task_name', 'task_description',
                  'task_start_time', 'task_end_time', 'task_is_done', 'task_project']
