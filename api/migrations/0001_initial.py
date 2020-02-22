# Generated by Django 3.0.3 on 2020-02-22 05:26

import api.enums
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('text', models.TextField(blank=True, null=True, verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('name', models.CharField(max_length=45)),
                ('next_course_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Course', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('name', models.CharField(max_length=45)),
                ('approval_score', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
                ('next_lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Lesson', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('fullname', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.TextField(blank=True, null=True, verbose_name='password')),
                ('type', models.CharField(choices=[(api.enums.UserType['STUDENT'], 'STUDENT'), (api.enums.UserType['TEACHER'], 'TEACHER'), (api.enums.UserType['ADMIN'], 'ADMIN')], default=api.enums.UserType['STUDENT'], max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('text', models.TextField(blank=True, null=True, verbose_name='text')),
                ('score', models.IntegerField()),
                ('type', models.CharField(choices=[(api.enums.QuestionType['BOOLEAN'], 'BOOLEAN'), (api.enums.QuestionType['ONE_ONLY'], 'ONE_ONLY'), (api.enums.QuestionType['MLTP_ONE'], 'MULTIPLE_ONE'), (api.enums.QuestionType['MLTP_ALL'], 'MULTIPLE_ALL')], default=api.enums.QuestionType['BOOLEAN'], max_length=45)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Lesson')),
            ],
        ),
    ]