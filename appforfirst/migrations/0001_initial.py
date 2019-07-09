# Generated by Django 2.0.13 on 2019-07-09 16:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_name', models.CharField(max_length=200)),
                ('diary_description', models.TextField(blank=True)),
                ('diary_data_utworzenia', models.DateTimeField(auto_now_add=True, null=True)),
                ('diary_start_data', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('diary_end_data', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('diary_wniosek', models.CharField(max_length=400)),
                ('diary_data_powrotu', models.DateTimeField(blank=True, null=True)),
                ('diary_custom_field1', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field2', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field3', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field4', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field5', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field6', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field7', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field8', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field9', models.CharField(blank=True, max_length=400)),
                ('diary_custom_field10', models.CharField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_description', models.TextField(blank=True)),
                ('project_creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('project_start_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('project_end_date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('project_status', models.CharField(choices=[('nowy_nieruszony', 'nowy'), ('in_progres', 'in_progres'), ('done_otwarty', 'done_otwarty'), ('done_zamkniety', 'done_zamkniety'), ('zawieszony', 'zawieszony')], max_length=50)),
                ('project_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_name', models.CharField(max_length=200)),
                ('reminder_description', models.TextField(blank=True)),
                ('reminder_data_utworzenia', models.DateTimeField(auto_now_add=True, null=True)),
                ('reminder_data_wykonania', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('reminder_is_done', models.BooleanField(default=False)),
                ('reminder_project', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='appforfirst.Project')),
                ('reminder_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[('spotkanie', 'spotkanie'), ('opłata', 'opłata'), ('todo', 'todo'), ('wyjazd', 'wyjazd'), ('inne', 'inne'), ('praca', 'praca')], max_length=50)),
                ('task_name', models.CharField(max_length=200)),
                ('task_description', models.TextField(blank=True)),
                ('task_data_utworzenia', models.DateTimeField(auto_now_add=True, null=True)),
                ('task_start_time', models.DateTimeField(blank=True, null=True)),
                ('task_end_time', models.DateTimeField(blank=True, null=True)),
                ('task_is_done', models.BooleanField(default=False)),
                ('task_project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='appforfirst.Project')),
                ('task_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='diary',
            name='diary_project',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='appforfirst.Project'),
        ),
        migrations.AddField(
            model_name='diary',
            name='diary_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
