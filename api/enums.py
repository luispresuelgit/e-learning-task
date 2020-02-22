from enum import Enum

# questionType = (
#     ('boolean', 'Boolean'),
#     ('one_only', 'Multiple choice where only one answer is correct'),
#     ('multiple_one', 'Multiple choice where more than one answer is correct'),
#     ('multiple_all', 'Multiple choice where more than one answer is correct and all of them must be answered correctly'),
# )
#
# userType = (
#     ('student', 'Student'),
#     ('teacher', 'Teacher'),
#     ('admin', 'administrator')
# )


class UserType(Enum):

    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    ADMIN = 'ADMIN'


class QuestionType(Enum):
    BOOLEAN = 'BOOLEAN'
    ONE_ONLY = 'ONE_ONLY'
    MLTP_ONE = 'MULTIPLE_ONE'
    MLTP_ALL = 'MULTIPLE_ALL'