### Description

    We require to develop an API for e-learning courses to integrate in our system. 
    The purpose of this tool is for us, as professors to manage courses configuration 
    and performance reviews and, for our students, to take courses when using our frontend. 
    Our PM is a very busy person, so we don’t have detailed tasks but only the business 
    rules to work with. Here they are:

### Instructions

    1. - We have courses that contain lessons and lessons that contain questions

    2. - The courses are correlative with previous ones

    3. - The lessons are correlative with previous ones

    4. - The questions for each lesson have no correlation

    5. - All questions for a lesson are mandatory

    6. - Each question has a score

    7. - Each lesson has an approval score that has to be met by the sum of correctly answered questions to approve it

    8. - A course is approved when all lessons are passed.

    9. - There’s no restriction on accessing approved courses

    10. - Only professors can create and manage courses, lessons and questions

    11. - Any student can take a course

    12. - Initially, we’ll need to support these types of questions:
        * Boolean
        * Multiple choice where only one answer is correct
        * Multiple choice where more than one answer is correct
        * Multiple choice where more than one answer is correct and all of them must be answered correctly

    13. - Frontend guys specifically asked for these endpoints for the students to use:
        * Get a list of all courses, telling which ones the student can access
        * Get lessons for a course, telling which ones the student can access
        * Get lesson details for answering its questions
        * Take a lesson (to avoid several requests, they asked to send all answers in one go)
        * Basic CRUD for courses, lessons and questions

### Codebase rules:

    1. The API must be developed using Python
    2. There must be a readme file documenting installation and usage.
    3. You must use Django. Also you  must include a readme file documenting libraries you used and its purpose 
    and a brief explanation with the reasoning for your choice.

### Technologies Used

**Django:** Asked to be used. \
**SQLite:** Brought by the default by Django. For this project, a robust relational database management system was not  
needed for demonstration also, its versatility with Djano allowed an easier and faster development.

## Installation instructions
```bash
python3 -m venv venv
. venv/bin/activate
pip install Django==3.0.3
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Usage

In order to mimic the feature for restrict usage for each endpoint access, a JSON field in the requests must be sent. 
Pending implement access token for future versions.

```
/api/courses/add POST -> {"user_type":"teacher"}
/api/courses/<course_id>/update PUT -> {"user_type":"teacher"}
/api/courses/<course_id>/lessons/add POST -> {"user_type":"teacher"}
/api/courses/<course_id>/lessons/<lesson_id>/update PUT -> {"user_type":"teacher"}
/api/courses/<course_id>/lessons/<lesson_id>/questions/add POST -> {"user_type":"teacher"}
/api/courses/<course_id>/lessons/<lesson_id>/questions/<question_id>/update PUT -> {"user_type":"teacher"}
```

**All endpoints:**

```
GET /api/users 
POST /api/users/add 
GET /api/users/<user_id> 
PUT /api/users/<user_id>/update 
DELETE /api/users/<user_id>/delete 
GET /api/users/<user_id>/course/<course_id> 
GET /api/users/<int:user_id>/course/<course_id>/lesson/<int:lesson_id> 
GET /api/courses
POST /api/courses/add 
GET /api/courses/<course_id> 
PUT /api/courses/<course_id>/update 
DELETE /api/courses/<course_id>/delete 
GET /api/courses/<course_id>/lessons 
POST /api/courses/<course_id>/lessons/add 
GET /api/courses/<course_id>/lessons/<lesson_id> 
PUT /api/courses/<course_id>/lessons/<lesson_id>/update 
DELETE /api/courses/<course_id>/lessons/<lesson_id>/delete 
GET /api/courses/<course_id>/lessons/<lesson_id>/questions 
POST /api/courses/<course_id>/lessons/<lesson_id>/questions/add 
GET/api/courses/<course_id>/lessons/<lesson_id>/questions/<question_id>  
PUT /api/courses/<course_id>/lessons/<lesson_id>/questions/<question_id>/update 
DELETE/api/courses/<course_id>/lessons/<lesson_id>/questions/<question_id>/delete 
POST /api/courses/<course_id>/lessons<lesson_id>/questions/answers 
```