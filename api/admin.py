from django.contrib import admin

from .models import Course, Lesson, Question

admin.site.register(Question)
admin.site.register(Course)
admin.site.register(Lesson)