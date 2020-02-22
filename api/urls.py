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

# urlpatterns = [
#     path('/courses', views.get_users, name='courses.index'),
#     path('/courses/<int:course_id>/', views.<define EP>, name='course.detail'),
#     path('/users', views.<define EP>, name='users.index'),
#     path('/users', views.<define EP>, name='users.create'),
#     path('/users/<int:user_id>', view-<define_EP>, name='user.detail'),
#     path('/users/<int:user_id>', view-<define_EP>, name='user.update'),
#     path('/users/<int:user_id>', view-<define_EP>, name='user.delete'),
#     path('/questions', views.<define EP>, name='questions.index'),
#     path('/questions', views.<define EP>, name='questions.create'),
#     path('/questions/<int:question_id>', view-<define_EP>, name='question.detail'),
#     path('/questions/<int:question_id>', view-<define_EP>, name='question.update'),
#     path('/questions/<int:question_id>', view-<define_EP>, name='question.delete'),
#     path('/questions/<int:question_id>/answers', view-<define_EP>, name='question.answers'),
#     path('/lessons', views.<define EP>, name='lessons.index'),
#     path('/lessons', views.<define EP>, name='lessons.create'),
#     path('/lessons/<int:lesson_id>', view-<define_EP>, name='lesson.detail'),
#     path('/lessons/<int:lesson_id>', view-<define_EP>, name='lesson.update'),
#     path('/lessons/<int:lesson_id>', view-<define_EP>, name='lesson.delete'),
#     path('/lessons/<int:lesson_id>/questions/<question_id>', view-<define_EP>, name='lesson.add_question_to_lesson'),
#     path('/lessons/<int:lesson_id>/next-lesson/<int:lesson_id>', view-<define_EP>, name='lesson.add_next_lesson_to_lesson'),
#     path('/courses', views.<define EP>, name='lessons.index'),
#     path('/courses', views.<define EP>, name='lessons.create'),
#     path('/courses/<int:course_id>', view-<define_EP>, name='course.detail'),
#     path('/courses/<int:course_id>', view-<define_EP>, name='course.update'),
#     path('/courses/<int:course_id>', view-<define_EP>, name='course.delete'),
#     path('/courses/<int:course_id>/lessons/<int:course_id>', view-<define_EP>, name='course.add_lesson_to_course'),
#     path('/courses/<int:course_id>/next-course/<int:course_id>', view-<define_EP>, name='course.add_next_course_to_course'),
# ]

urlpatterns = [
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users', views.get_users, name='users.index'),
    path('users/add', views.add_user, name='users.create'),
    path('users/<int:user_id>', views.get_user, name='user.detail'),
    path('users/<int:user_id>/update', views.update_user, name='user.update'),
    path('users/<int:user_id>/delete', views.delete_user, name='user.delete'),
]