
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TASK_TYPE = [
    ('spotkanie', 'spotkanie'),
    ('opłata', 'opłata'),
    ('todo', 'todo'),
    ('wyjazd', 'wyjazd'),
    ('inne', 'inne'),
    ('praca','praca')
]

PROJECT_STATUS = [
    ('nowy_nieruszony', 'nowy'),
    ('in_progres', 'in_progres'),
    ('done_otwarty', 'done_otwarty'),
    ('done_zamkniety', 'done_zamkniety'),
    ('zawieszony', 'zawieszony')
]

class Project(models.Model):
    project_user = models.ForeignKey(User, on_delete=models.PROTECT)
    project_name = models.CharField(max_length=50)
    project_description = models.TextField(blank=True)
    project_creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    project_start_date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    project_end_date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    project_status = models.CharField(choices=PROJECT_STATUS, max_length=50)

    def __str__(self):
        return self.project_name

#Zadania
class Tasks(models.Model):
    task_user = models.ForeignKey(User, on_delete=models.PROTECT)
    task_type = models.CharField(choices=TASK_TYPE, max_length=50)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField(blank=True)
    task_data_utworzenia = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    task_start_time = models.DateTimeField(null=True, blank=True)
    task_end_time = models.DateTimeField(null=True, blank=True)
    task_is_done = models.BooleanField(default=False)
    task_project = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.task_name

#Dziennik
class Diary(models.Model):
    diary_user = models.ForeignKey(User, on_delete=models.PROTECT)
    diary_name = models.CharField(max_length=200)
    diary_description = models.TextField(blank=True)
    diary_data_utworzenia = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    diary_start_data = models.DateTimeField(default=datetime.now, null=True, blank=True)
    diary_end_data = models.DateTimeField(default=datetime.now, null=True, blank=True)
    diary_wniosek = models.CharField(max_length=400)
    diary_data_powrotu = models.DateTimeField(null=True, blank=True)
    diary_project = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True, default=None)
    diary_custom_field1 = models.CharField(max_length=400, blank=True)
    diary_custom_field2 = models.CharField(max_length=400, blank=True)
    diary_custom_field3 = models.CharField(max_length=400, blank=True)
    diary_custom_field4 = models.CharField(max_length=400, blank=True)
    diary_custom_field5 = models.CharField(max_length=400, blank=True)
    diary_custom_field6 = models.CharField(max_length=400, blank=True)
    diary_custom_field7 = models.CharField(max_length=400, blank=True)
    diary_custom_field8 = models.CharField(max_length=400, blank=True)
    diary_custom_field9 = models.CharField(max_length=400, blank=True)
    diary_custom_field10 = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.diary_name

#Przypominajka
class Reminder(models.Model):
    reminder_user = models.ForeignKey(User, on_delete=models.PROTECT)
    reminder_name = models.CharField(max_length=200)
    reminder_description = models.TextField(blank=True)
    reminder_data_utworzenia = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    reminder_data_wykonania = models.DateTimeField(default=datetime.now, null=True, blank=True)
    reminder_is_done = models.BooleanField(default=False)
    reminder_project = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True, default=None)

    def __str__(self):
        return self.reminder_name
