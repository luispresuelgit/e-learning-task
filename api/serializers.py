from rest_framework import serializers
from .models import Course, Lesson, Question, Answer, User


# class UserSerializer(serializers.Serializer):
#      id = serializers.ReadOnlyField()
#      fullname = serializers.CharField()
#      username = serializers.CharField()
#      password = serializers.TextField()
#
#      def create(self, validate_data):
#          user = User()
#          user.fullname = validate_data.get("fullname")
#          user.username = validate_data.get("username")
#          user.password.set_password(validate_data.get("password"))
#          user.save()
#          return user
#
#      def validate_username(self, data):
#          user = User.objects.filter(username = data)
#          if len(users) != 0:
#              raise serializers.ValidationError("This username already exists. Try another one")
#          else:
#              return data


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
