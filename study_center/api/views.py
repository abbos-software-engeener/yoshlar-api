from import_export.formats.base_formats import JSON
from rest_framework.generics import *
from .serilaizers import *
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from rest_framework.response import Response


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=JSON):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class TeacherView(ListAPIView):
    queryset = AboutTeacher.objects.all()
    serializer_class = TeacherSerializer


class CourseView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            queryset = Course.objects.get(pk=pk)
            serializer = CourseSerializer(queryset)
        else:
            queryset = Course.objects.all()
            serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CoursRegisterView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            queryset = CourseRegister.objects.get(pk=pk)
            serializer = CRegisterSerializer(queryset)
        else:
            queryset = CourseRegister.objects.all()
            serializer = CRegisterSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        course = CourseRegister.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = CourseRegister.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class TrainingView(CreateAPIView,RetrieveUpdateDestroyAPIView):
    def get(self, request, pk=None):
        if pk is not None:
            queryset = Training.objects.get(pk=pk)
            serializer = TrainingSerializer(queryset)
        else:
            queryset = Training.objects.all()
            serializer = TrainingSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        course = Training.objects.get(pk=pk)
        serializer = TrainingSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = Training.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrainingRegisterView(APIView):
    def get(self, request):

        queryset = TrainingRegister.objects.filter(first_name__icontains=request.GET.get("q", ""))
        serializer = TrainingRegistrationSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainingRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        course = TrainingRegister.objects.get(pk=pk)
        serializer = TrainingRegistrationSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = TrainingRegister.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

