from  rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTeacher
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegister
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"


class TrainingRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingRegister
        fields = "__all__"


# class DashboardSerializer(serializers.Serializer):
#     AboutTeacher = TeacherSerializer(required=False,many=True)



