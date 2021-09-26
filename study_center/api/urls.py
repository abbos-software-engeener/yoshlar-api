from django.urls import path, include

from .views import *

app_name = 'api'


urlpatterns = [
    path("", TeacherView.as_view()),
    path('course-register/', CoursRegisterView.as_view()),
    path('course-register/<int:pk>/', CoursRegisterView.as_view()),
    path('course/', CourseView.as_view()),
    path('course/<int:pk>/',  CourseView.as_view()),
    path('traningregister/', TrainingRegisterView.as_view()),
    path('traningregister/<int:pk>/', TrainingRegisterView.as_view()),
    path("dashboard/", include("client.urls"))
]