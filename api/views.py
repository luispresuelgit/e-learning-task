from .models import Course, Lesson, Question, Answer, User
from .serializers import CourseSerializer, LessonSerializer, QuestionSerializer, UserSerializer
from django.http import JsonResponse
import json
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from .enums import UserType, QuestionType
import copy

### users ####


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        queryset = User.objects.all().values()
        users = list(queryset)
        return JsonResponse(users, safe=False)

@api_view(['POST'])
def add_user(request):
    data = json.loads(request.body)
    switch = {
        "student": UserType.STUDENT.name,
        "teacher": UserType.TEACHER.name,
        "admin": UserType.ADMIN.name
    }
    user_type = switch.get(data['type'])
    user = User(email=data['email'],
                fullname=data['fullname'],
                password=make_password(data['password']),
                type=user_type)
    user.save()
    users_serialized = UserSerializer(user)
    return JsonResponse(users_serialized.data, safe=False)

def get_user(request, user_id):
    if request.method == 'GET':
        user = User.objects.filter(id=user_id).first()
        user = UserSerializer(user)
        return JsonResponse(user.data, safe=False)

@api_view(['PUT'])
def update_user(request, user_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        user = User.objects.filter(id=user_id).first()
        if {'fullname'}.issubset(set(data)):
            user.fullname = data['fullname']
        if {'email'}.issubset(set(data)):
            user.email = data['email']
        if {'password'}.issubset(set(data)):
            user.password = make_password(data['password'])
        user.save()
        user = UserSerializer(user)
        return JsonResponse(user.data, safe=False)

@api_view(['DELETE'])
def delete_user(request, user_id):
    response = {}
    user = User.objects.filter(id=user_id).first()
    user_serialized = UserSerializer(user)
    user_copy = copy.deepcopy(user_serialized)
    response['response'] = 'Successfully deleted user'
    response['user'] = user_copy.data
    user.delete()
    return JsonResponse(response)

@api_view(['GET'])
def user_add_course(request, user_id, course_id):
    user = User.objects.filter(id=user_id).first()
    course = Course.objects.filter(id=course_id).first()
    last_course = user.courses[len(user.courses)]
    if last_course is not None: # Otherwise would mean is the first one
        if course_id != last_course.next_course_id:
            # meaning the current course is not the corresponding one (correlation between courses)
            return JsonResponse({"message":"Error, current course trying to be added is not related to the previous course"})
    user.courses.append(course)
    user.save()
    user = UserSerializer(user)
    return JsonResponse(user.data, safe=False)

@api_view(['GET'])
def user_add_lesson(request, user_id, course_id, lesson_id):
    user = User.objects.filter(id=user_id).first()
    course = Course.objects.filter(lesson__in=Lesson.objects.filter(id=lesson_id)).first() # should be unique
    if course is None:
        return JsonResponse({"message": "Error, current lesson id: %s does not belong to this course %s" % (
            lesson_id, course_id
        )})
    lesson = Lesson.objects.filter(id=lesson_id).first()
    last_lesson = user.courses[len(user.lessons)]
    if last_lesson is not None: # Otherwise would mean is the first one
        if lesson_id != last_lesson.next_lesson_id:
            # meaning the current course is not the corresponding one (correlation between courses)
            return JsonResponse({"message":"Error, current lesson trying to be added is not related to the previous lesson"})
    user.lessons.append(lesson)
    user.save()
    user = UserSerializer(user)
    return JsonResponse(user.data, safe=False)

# ### question ###

@api_view(['GET'])
def get_questions(request, course_id, lesson_id):
    if request.method == 'GET':
        queryset = Question.objects.filter(lesson__in=Lesson.objects.filter(id=lesson_id)).all().values()
        questions = list(queryset)
        return JsonResponse(questions, safe=False)

@api_view(['POST'])
def add_question(request, course_id, lesson_id):
    lesson = Lesson.Objects.filter(id=lesson_id).first()
    data = json.loads(request.body)
    if data['user_type'] == 'teacher':
        switch = {
            "boolean": QuestionType.BOOLEAN.name,
            "one_only": QuestionType.ONE_ONLY.name,
            "multiple_one": QuestionType.MLTP_ONE.name
            "multiple_all": QuestionType.MLTP_ALL.name
        }
        question_type = switch.get(data['type'])
        question = Question(text=data['text'],
                    score=data['score'],
                    type=question_type,
                    lesson=lesson)
        question.save()
        questions_serialized = QuestionSerializer(question)
        return JsonResponse(questions_serialized.data, safe=False)
    else:
        return JsonResponse({"message": "No Allowed Action"})

def get_question(request, course_id, lesson_id, question_id):
    if request.method == 'GET':
        question = Question.objects.filter(id=question_id).first()
        question = UserSerializer(question)
        return JsonResponse(question.data, safe=False)

@api_view(['PUT'])
def update_question(request, course_id, lesson_id, question_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        if data['user_type'] == 'teacher':
            question = Question.objects.filter(id=question_id).first()
            if {'text'}.issubset(set(data)):
                question.text = data['text']
            if {'score'}.issubset(set(data)):
                question.score = data['score']
            if {'type'}.issubset(set(data)):
                switch = {
                    "boolean": QuestionType.BOOLEAN.name,
                    "one_only": QuestionType.ONE_ONLY.name,
                    "multiple_one": QuestionType.MLTP_ONE.name
                    "multiple_all": QuestionType.MLTP_ALL.name
                }
                question_type = switch.get(data['type'])
                question.type = question_type

            question.save()
            question = QuestionSerializer(question)
            return JsonResponse(question.data, safe=False)
        else:
            return JsonResponse({"message": "No Allowed Action"})

@api_view(['DELETE'])
def delete_question(request, course_id, lesson_id, question_id):
    response = {}
    question = Question.objects.filter(id=question_id).first()
    question_serialized = QuestionSerializer(question)
    question_copy = copy.deepcopy(question_serialized)
    response['response'] = 'Successfully deleted question'
    response['question'] = question_copy.data
    question.delete()
    return JsonResponse(response)

@api_view(['POST'])
def add_answer_questions(request, course, lesson_id):
    # We currently are not using the bulk_create func by DJango because we want to add the relationship for answers
    answers = []
    answers_data = json.loads(request.body) # they should be passed as a list in the JSON data
    lesson = Lesson.Objects.filter(id=lesson_id).first()
    for answer_data in answers_data:
        answer = Answer(
            answer_data['text'],
            lesson=lesson
        )
        answer.save()
        answers.append(answer)
    return JsonResponse(answers, safe=False)

# ### lesson ###

@api_view(['GET'])
def get_lessons(request, course_id):
    if request.method == 'GET':
        queryset = Lesson.objects.filter(course__in=Course.objects.filter(id=course)).all().values()
        lessons = list(queryset)
        return JsonResponse(lessons, safe=False)

@api_view(['POST'])
def add_lesson(request, course_id):
    data = json.loads(request.body)
    if data['user_type'] == 'teacher':
        course = Course.Objects.filter(id=course_id).first()
        lesson = Lesson(name=data['name'],
                        approval_score=data['score'],
                        course=course)
        lesson.save()
        current_course_id = lesson.course.id
        prev_lesson = Lesson.objects.filter(id=(lesson.id-1)).first()
        if prev_lesson is not None:
            prev_course_id = prev_lesson.course.id
            if current_course_id == prev_course_id: # meaning this lesson it's not the first one for the current course
                prev_lesson.next_lesson_id = lesson.id

        lessons_serialized = LessonSerializer(lesson)
        return JsonResponse(lessons_serialized.data, safe=False)
    else:
        return JsonResponse({"message": "No Allowed Action"})

def get_lesson(request, course_id, lesson_id):
    if request.method == 'GET':
        lesson = Lesson.Objects.filter(id=lesson_id).first()
        lesson = LessonSerializer(lesson)
        return JsonResponse(lesson.data, safe=False)

@api_view(['PUT'])
def update_lesson(request, course_id, lesson_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        if data['user_type'] == 'teacher':
            lesson = Lesson.objects.filter(id=lesson_id).first()
            if {'name'}.issubset(set(data)):
                lesson.name = data['name']
            if {'approval_score'}.issubset(set(data)):
                lesson.approval_score = data['approval_score']
            lesson.save()
            lesson = LessonSerializer(lesson)
            return JsonResponse(lesson.data, safe=False)
        else:
            return JsonResponse({"message": "No Allowed Action"})

@api_view(['DELETE'])
def delete_lesson(request, course_id, lesson_id):
    response = {}
    lesson = Lesson.objects.filter(id=lesson_id).first()
    lesson_serialized = LessonSerializer(lesson)
    lesson_copy = copy.deepcopy(lesson_serialized)
    response['response'] = 'Successfully deleted lesson'
    response['lesson'] = lesson_copy.data
    lesson.delete()
    return JsonResponse(response)

# ### course ###

@api_view(['GET'])
def get_courses(request):
    if request.method == 'GET':
        queryset = Course.objects.all().values()
        courses = list(queryset)
        return JsonResponse(courses, safe=False)

@api_view(['POST'])
def add_course(request):
    data = json.loads(request.body)
    if data['user_type'] == 'teacher':
        course = Course(name=data['name'])
        course.save()
        # get previous course
        pre_course = Course.objects.filter(id=(course.id-1)).first()
        if pre_course is not None:
            # means is not the first one, so we need to add the next_course_id
            pre_course.next_course_id = course.id
            pre_course.save()
        course_serialized = CourseSerializer(course)
        return JsonResponse(course_serialized.data, safe=False)
    else:
        return JsonResponse({"message": "No Allowed Action"})

def get_course(request, course_id):
    if request.method == 'GET':
        course = Course.Objects.filter(id=course_id).first()
        course = CourseSerializer(course)
        return JsonResponse(course.data, safe=False)


@api_view(['PUT'])
def update_course(request, course_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        if data['user_type'] == 'teacher':
            course = Lesson.objects.filter(id=course_id).first()
            if {'name'}.issubset(set(data)):
                course.name = data['name']
            course.save()
            course = CourseSerializer(course)
            return JsonResponse(course.data, safe=False)
        else:
            return JsonResponse({"message": "No Allowed Action"})

@api_view(['DELETE'])
def delete_course(request, course_id):
    response = {}
    course = Course.objects.filter(id=course_id).first()
    course_serialized = CourseSerializer(course)
    course_copy = copy.deepcopy(course_serialized)
    response['response'] = 'Successfully deleted course'
    response['course'] = course_copy.data
    course.delete()
    return JsonResponse(response)