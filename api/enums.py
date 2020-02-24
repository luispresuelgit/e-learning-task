from enum import Enum


class UserType(Enum):

    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    ADMIN = 'ADMIN'


class QuestionType(Enum):
    BOOLEAN = 'BOOLEAN'
    ONE_ONLY = 'ONE_ONLY'
    MLTP_ONE = 'MULTIPLE_ONE'
    MLTP_ALL = 'MULTIPLE_ALL'