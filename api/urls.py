from django.urls import path

from . import views

from rest_framework.authtoken.views import obtain_auth_token

### courses ###

# /api/courses
# /api/courses/<course_id>/

### users ###

# /api/users GET
# /api/users POST
# /api/users/<user_id> GET
# /api/users/<user_id> PUT
# /api/users/<user_id> DELETE

### questions ###

# /api/questions GET
# /api/questions POST
# /api/questions/<questions_id> GET
# /api/questions/<questions_id> PUT
# /api/questions/<question_id> DELETE
# /api/question/<question_id>/answers POST

### lessons ###

# /api/lessons GET
# /api/lessons POST
# /api/lessons/<lesson_id> GET
# /api/lessons/<lesson_id> PUT
# /api/lessons/<lesson_id> DELETE
# /api/lessons/<lesson_id>/questions/<question_id> GET
# /api/lessons/<lesson_id>/next-lesson/<next_lesson_id> GET

### courses ###

# /api/courses GET
# /api/courses POST
# /api/courses/<course_id> GET
# /api/courses/<course_id> PUT
# /api/courses/<course_id> DELETE
# /api/course/<course_id>/lessons/<lesson_id> GET
# /api/course/<course_id>/next-course/<next_course_id> GET

app_name = 'api'

urlpatterns = [
    # path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users', views.get_users, name='users.index'),
    path('users/add', views.add_user, name='users.create'),
    path('users/<int:user_id>', views.get_user, name='user.detail'),
    path('users/<int:user_id>/update', views.update_user, name='user.update'),
    path('users/<int:user_id>/delete', views.delete_user, name='user.delete'),
    path('users/<int:user_id>/course/<int:course_id>', views.user_add_course, name='user.add_course'),
    path('users/<int:user_id>/course/<int:course_id>/lesson/<int:lesson_id>', views.user_add_lesson, name='user.add_lesson'),
    path('users/<int:user_id>/delete', views.delete_user, name='user.delete'),
    path('/courses', views.get_courses, name='courses.index'),
    path('/courses/add', views.add_course, name='courses.create'),
    path('/courses/<int:course_id>', views.get_course, name='course.detail'),
    path('/courses/<int:course_id>/update', views.update_course, name='course.update'),
    path('/courses/<int:course_id>/delete', views.delete_course, name='course.delete'),
    path('/courses/<int:course_id>/lessons', views.get_lessons, name='lessons.index'),
    path('/courses/<int:course_id>/lessons<int:lesson_id>', views.get_lesson, name='lesson.detail'),
    path('/courses/<int:course_id>/lessons<int:lesson_id>/update', views.update_lesson, name='lesson.update'),
    path('/courses/<int:course_id>/lessons<int:lesson_id>/delete', views.delete_lesson, name='lesson.delete'),
    path('/courses/<int:course_id>/lessons<int:lesson_id>/questions', views.get_questions, name='questions.index'),
    path('/courses/<int:course_id>/lessons<int:lesson_id>/questions/<int:question_id>', views.get_question, name='question.detail'),
    path('/courses/<int:course_id>/lessons<int:lesson_id>/questions/<int:question_id>/update', views.update_question, name='question.update'),
    path('/courses/<int:course_id>/lessons<int:lesson_id>/questions/<int:question_id>/delete', views.delete_question, name='question.delete'),
    path('/courses/<int:course_id>/lessons<int:lesson_id>/questions/answers', views.add_answer_questions, name='questions.answers'),
]