from django.contrib import admin
from appforfirst.models import Tasks, Diary, Project, Reminder

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Diary)
admin.site.register(Project)
admin.site.register(Reminder)
