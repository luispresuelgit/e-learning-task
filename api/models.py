from django.db import models
from .enums import UserType, QuestionType


class Course(models.Model):
    created = models.DateTimeField('date published', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)
    next_course_id = models.IntegerField()
    name = models.CharField(max_length=45)
    user = models.ForeignKey('User', related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        self.name


class Lesson(models.Model):
    created = models.DateTimeField('date published', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)
    next_lesson_id = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)  # We assume a lesson name shouldn't be too long
    approval_score = models.IntegerField()
    user = models.ForeignKey('User', related_name='lessons', on_delete=models.CASCADE)

    def __str__(self):
        self.name


class Question(models.Model):
    created = models.DateTimeField('date published', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text = models.TextField("text", null=True, blank=True)
    score = models.IntegerField()
    type = models.CharField(
        max_length=45,
        choices=[(tag, tag.value) for tag in QuestionType],
        default=QuestionType.BOOLEAN
    )

    def __str__(self):
        self.text


class Answer(models.Model):
    created = models.DateTimeField('date published', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)
    text = models.TextField("text", null=True, blank=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        self.text


class User(models.Model):
    created = models.DateTimeField('date published', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)
    fullname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.TextField("password", null=True, blank=True)
    type = models.CharField(
        max_length=45,
        choices=[(tag, tag.value) for tag in UserType],
        default=UserType.STUDENT
    )

    # def __str__(self):
    #     self.email