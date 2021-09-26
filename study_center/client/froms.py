from django import forms
from api.models import *


class AboutTeacherForm(forms.ModelForm):
    class Meta:
        model = AboutTeacher()
        fields = '__all__'


class CourseRegisterForm(forms.ModelForm):
    class Meta:
        model = CourseRegister()
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseRegister()
        fields = '__all__'


class TrainingForm(forms.ModelForm):
    class Meta:
        model = CourseRegister()
        fields = '__all__'


class TrainingRegisterForm(forms.ModelForm):
    class Meta:
        model = CourseRegister()
        fields = '__all__'