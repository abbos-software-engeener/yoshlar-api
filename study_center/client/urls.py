from django.urls import path
from . import views

app_name = 'client'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category_list/', views.category_list, name="category_list"),
    path('category_create/', views.category_create, name="category_create"),
    path('<int:pk>category_edit/', views.category_edit, name="category_edit"),
    path('<int:pk>/category_delete/', views.category_delete, name="category_delete"),

    path('registerr_list/', views.registerr_list, name="registerr_list"),
    path('registerr_create/', views.registerr_create, name="registerr_create"),
    path('<int:pk>registerr_edit/', views.registerr_edit, name="registerr_edit"),
    path('<int:pk>/registerr_delete/', views.registerr_delete, name="registerr_delete"),

    path('course_list/', views.course_list, name="course_list"),
    path('course_create/', views.course_create, name="course_create"),
    path('<int:pk>course_edit/', views.course_edit, name="course_edit"),
    path('<int:pk>/course_delete/', views.course_delete, name="course_delete"),

    path('training_list/', views.training_list, name="training_list"),
    path('training_create/', views.training_create, name="training_create"),
    path('<int:pk>training_edit/', views.training_edit, name="training_edit"),
    path('<int:pk>/training_delete/', views.training_delete, name="training_delete"),

    path('register_list/', views.register_list, name="register_list"),
    path('register_create/', views.register_create, name="register_create"),
    path('<int:pk>register_edit/', views.register_edit, name="register_edit"),
    path('<int:pk>/register_delete/', views.register_delete, name="register_delete"),
    
]
