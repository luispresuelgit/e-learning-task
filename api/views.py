from django.http import HttpResponse
# from rest_framework import generics
from .models import Course, Lesson, Question, Answer, User
# from .enums import userType
from .serializers import CourseSerializer, LessonSerializer, QuestionSerializer, AnswerSerializer, UserSerializer
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from .enums import UserType
from django.core import serializers
import copy

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        # users = User.objects.all().values()
        # users = list(users)
        # data = json.dumps(users, indent=4, sort_keys=True, default=str)
        # return HttpResponse(content=data)

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
    print("user: %s" % user)
    user_serialized = UserSerializer(user)
    user_copy = copy.deepcopy(user_serialized)
    print("user_copy: %s" % user_copy)
    response['response'] = 'Successfully deleted user'
    response['user'] = user_copy.data
    user.delete()
    return JsonResponse(response)


# def user_add_course():

# @app.route('/user/<user_id>/first-course', methods=['GET'])
# def user_first_course(user_id):
# 	user = User.objects(id=user_id).get()
# 	first_course = User.objects().first()
# 	user.available_courses.append(first_course)
# 	user.save()
# 	return jsonify({'first_course': first_course.name})
#
# @app.route('/user/<user_id>/first-lesson', methods=['GET'])
# def user_first_course(user_id):
# 	user = User.objects(id=user_id).get()
# 	first_course = Courses.objects().first()
# 	first_lesson = first_course.lessons.first()
# 	user.available_lessons.append(first_lesson)
# 	user.save()
# 	return jsonify({'first_lesson': first_lesson.name})
#
# @app.route('/user/<user_id>/available-courses/<course_id>', methods=['GET'])
# def add_course_to_available_courses(user_id, course_id):
# 	user = User.objects(id=user_id).get()
# 	course = Course.objects(id=course_id).get()
# 	user.available_courses.append(course)
# 	user.save()
# 	return jsonify({
# 		'message': f'Course {course.name} added to available courses of {user.name}.'
# 	})
#
# @app.route('/user/<user_id>/available-lessons/<lesson_id>', methods=['GET'])
# def add_lesson_to_available_lessons(user_id, lesson_id):
# 	user = User.objects(id=user_id).get()
# 	lesson = Lesson.objects(id=lesson_id).get()
# 	user.available_lessons.append(lesson)
# 	user.save()
# 	last_course = user.available_courses[-1]
# 	lessons_in_last_course = last_course.lessons
# 	total_lessons_in_last_course = len(lessons_in_last_course)
# 	total_available_lessons = len(user.available_lessons)
# 	if total_available_lessons == total_lessons_in_last_course:
# 		del user.available_lessons[:]
# 		next_course = last_course.next_course_id
# 		user.available_courses.append(next_course)
# 		next_lesson = next_course.lessons[0]
# 		user.available_lessons.append(next_lesson)
# 		user.save()
# 		return jsonify({
# 			'message': f'New course {next_course.name} and new {next_lesson.name}.'
# 		})
# 	next_lesson = lesson.next_lesson_id
# 	user.available_lessons.append(next_lesson)
# 	user.save()
# 	return jsonify({
# 		'message': f'Added lesson {next_lesson.name} to available lessons of {user.name}.'
# 	})
#
# ### question ###
#
# @app.route('/question')
# def get_questions():
# 	question_data = Question.get_all()
# 	return jsonify({'questions': question_data})
#
# @app.route('/question', methods=['POST'])
# def add_question():
# 	data = request.get_json()
# 	question = Question(text=data['text'],
# 						detail=data['detail'],
# 						score=data['score'],
# 						question_type=data['question_type'])
# 	question.save()
# 	return jsonify({'new_question': question.json()})
#
# @app.route('/question/<question_id>', methods=['GET'])
# def get_question(question_id):
# 	question = Question.objects(id=question_id).get()
# 	return jsonify({'question': question.json()})
#
# @app.route('/question/<question_id>', methods=['PUT'])
# def update_question(question_id):
# 	data = request.get_json()
# 	question = Question.objects(id=question_id).get()
# 	question.update(
# 		text=data['text'],
# 		detail=data['detail'],
# 		score=data['score'],
# 		question_type=data['question_type'])
# 	question.reload()
# 	return jsonify({'updated_question': question.json()})
#
# @app.route('/question/<question_id>', methods=['DELETE'])
# def delete_question(question_id):
# 	question = Question.objects(id=question_id).get()
# 	question_text = question.text
# 	question.delete()
# 	return jsonify({'deleted_question': question_text})
#
# # POST /question/<question_id>/answers
# @app.route('/question/<question_id>/answers', methods=['POST'])
# def add_answer_to_question(question_id):
# 	data = request.get_json()
# 	question = Question.objects(id=question_id).get()
# 	answer = Answer(text=data['text'],
# 					correct=data['correct'])
# 	question.answers.append(answer)
# 	question.save()
# 	return jsonify({
# 		'message': f'Answer {answer.text} added to question {question.text}.'
# 	})
#
# ### lesson ###
#
# @app.route('/lesson')
# def get_lessons():
# 	lesson_data = Lesson.get_all()
# 	return jsonify({'lessons': lesson_data})
#
# @app.route('/lesson', methods=['POST'])
# def add_lesson():
# 	data = request.get_json()
# 	lesson = Lesson(name=data['name'],
# 					approval_score=data['approval_score'])
# 	lesson.save()
# 	return jsonify({'new_lesson': lesson.json()})
#
# @app.route('/lesson/<lesson_id>', methods=['GET'])
# def get_lesson(lesson_id):
# 	lesson = Lesson.objects(id=lesson_id).get()
# 	return jsonify({'lesson': lesson.json()})
#
# @app.route('/lesson/<lesson_id>', methods=['PUT'])
# def update_lesson(lesson_id):
# 	data = request.get_json()
# 	lesson = Lesson.objects(id=lesson_id).get()
# 	lesson.update(
# 		name=data['name'],
# 		approval_score=data['approval_score']
# 	)
# 	lesson.reload()
# 	return jsonify({'updated_lesson': lesson.json()})
#
# @app.route('/lesson/<lesson_id>', methods=['DELETE'])
# def delete_lesson(lesson_id):
# 	lesson = Lesson.objects(id=lesson_id).get()
# 	questions = lesson.questions
# 	for question in questions:
# 		question.delete()
# 	lesson_name = lesson.name
# 	lesson.delete()
# 	return jsonify({'deleted_lesson': lesson_name})
#
# @app.route('/lesson/<lesson_id>/question/<question_id>', methods=['GET'])
# def add_question_to_lesson(lesson_id, question_id):
# 	lesson = Lesson.objects(id=lesson_id).get()
# 	lesson_name = lesson.name
# 	question = Question.objects(id=question_id).get()
# 	question_text = question.text
# 	lesson.questions.append(question)
# 	lesson.save()
# 	return jsonify({
# 		'message': f'Question {question.text} added to lesson {lesson.name}.'
# 	})
#
# @app.route('/lesson/<lesson_id>/next-lesson/<next_lesson_id>', methods=['GET'])
# def add_next_lesson_to_lesson(lesson_id, next_lesson_id):
# 	lesson = Lesson.objects(id=lesson_id).get()
# 	next_lesson_id = Lesson.objects(id=next_lesson_id).get()
# 	lesson.next_lesson_id = next_lesson_id
# 	lesson.save()
# 	return jsonify({
# 		'message': f'Next lesson {next_lesson_id.name} added to lesson {lesson.name}.'
# 	})
#
# @app.route('/lesson/<lesson_id>/full', methods=['GET'])
# def get_lesson_full(lesson_id):
# 	lesson = Lesson.objects(id=lesson_id).get()
# 	return jsonify({'lesson': lesson.json_full()})
#
# ### course ###
#
# @app.route('/course')
# def get_courses():
# 	course_data = Course.get_all()
# 	return jsonify({'courses': course_data})
#
# @app.route('/course', methods=['POST'])
# def add_course():
# 	data = request.get_json()
# 	course = Course(name=data['name'])
# 	course.save()
# 	return jsonify({'new_course': course.json()})
#
# @app.route('/course/<course_id>', methods=['GET'])
# def get_course(course_id):
# 	course = Course.objects(id=course_id).get()
# 	return jsonify({'course': course.json()})
#
# @app.route('/course/<course_id>', methods=['PUT'])
# def update_course(course_id):
# 	data = request.get_json()
# 	course = Course.objects(id=course_id).get()
# 	course.update(
# 		name=data['name']
# 	)
# 	course.reload()
# 	return jsonify({'updated_course': course.json()})
#
# @app.route('/course/<course_id>', methods=['DELETE'])
# def delete_course(course_id):
# 	course = Course.objects(id=course_id).get()
# 	lessons = course.lessons
# 	for lesson in lessons:
# 		lesson.delete()
# 	course_name = course.name
# 	course.delete()
# 	return jsonify({'deleted_course': course_name})
#
# @app.route('/course/<course_id>/lesson/<lesson_id>', methods=['GET'])
# def add_lesson_to_course(course_id, lesson_id):
# 	course = Course.objects(id=course_id).get()
# 	course_name = course.name
# 	lesson = Lesson.objects(id=lesson_id).get()
# 	lesson_name = lesson.name
# 	course.lessons.append(lesson)
# 	course.save()
# 	return jsonify({
# 		'message': f'Lesson {lesson.name} added to course {course.name}.'
# 	})
#
# @app.route('/course/<course_id>/next-course/<next_course_id>', methods=['GET'])
# def add_next_course_to_course(course_id, next_course_id):
# 	course = Course.objects(id=course_id).get()
# 	next_course_id = Course.objects(id=next_course_id).get()
# 	course.next_course_id = next_course_id
# 	course.save()
# 	return jsonify({
# 		'message': f'Next course {next_course_id.name} added to course {course.name}.'
# 	})
#
# if __name__ == '__main__':
#     app.run(debug=True)