from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .froms import *
from api.serilaizers import *


def login_required_decorator(f):
    return login_required(f, login_url="client:login")

@login_required_decorator
def dashboard(request):
    return render(request, 'dashboard/index.html')

def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('client:dashboard')
    return render(request, 'dashboard/login.html')

@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('client:login')



@login_required_decorator
def category_list(request):
    aboutteacher = AboutTeacher.objects.all()
    print(aboutteacher)
    ctx = {
        'aboutteacher': aboutteacher,
        "c_active": 'active'
    }

    return render(request, 'dashboard/categories/list.html', ctx)


@login_required_decorator
def category_create(request):
    model = AboutTeacher()
    form = AboutTeacherForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)


@login_required_decorator
def category_edit(request, pk):
    model = AboutTeacher.objects.all()[0]
    form = AboutTeacherForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:category_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/categories/form.html', ctx)


@login_required_decorator
def category_delete(request, pk):
    model = AboutTeacher.objects.get(id=pk)
    model.delete()
    return redirect('client:register_list')






@login_required_decorator
def registerr_list(request):
    courseregister = CourseRegister.objects.all()
    ctx = {
        'courseregister': courseregister,
        "i_active": 'active'
    }
    return render(request,'dashboard/CourseRegister/list.html',ctx)

@login_required_decorator
def registerr_create(request):
    model = CourseRegister()
    form = CourseRegisterForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:registerr_create')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/CourseRegister/form.html', ctx)

@login_required_decorator
def registerr_edit(request, pk):
    model = CourseRegister.objects.get(id=pk)
    form = CourseRegisterForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:registerr_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/CourseRegister/form.html', ctx)

@login_required_decorator
def registerr_delete(request, pk):
    model = CourseRegister.objects.get(id=pk)
    model.delete()
    return redirect('client:registerr_delete')





@login_required_decorator
def course_list(request):
    course = Course.objects.all()
    ctx = {
        'course': course,
        "a_active": 'active'
    }
    return render(request,'dashboard/Course/list.html',ctx)

@login_required_decorator
def course_create(request):
    model = Course()
    form = CourseForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('main:course_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/Course/form.html', ctx)

@login_required_decorator
def course_edit(request, pk):
    model = Course.objects.get(id=pk)
    form = CourseForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:course_edit')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def course_delete(request, pk):
    model = Course.objects.get(id=pk)
    model.delete()
    return redirect('client:product_list')




@login_required_decorator
def training_list(request):
    training = Training.objects.all()
    ctx = {
        'training': training,
        "u_active": 'active'
    }
    return render(request,'dashboard/Training/list.html',ctx)

@login_required_decorator
def training_create(request):
    model = Training()
    form = TrainingForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def training_edit(request, pk):
    model = Training.objects.get(id=pk)
    form = TrainingForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:product_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def training_delete(request, pk):
    model = Training.objects.get(id=pk)
    model.delete()
    return redirect('client:product_list')





@login_required_decorator
def register_list(request):
    trainingregister = TrainingRegister.objects.all()
    ctx = {
        'trainingregister': trainingregister,
        "o_active": 'active'
    }
    return render(request,'dashboard/TrainingRegister/list.html',ctx)

@login_required_decorator
def register_create(request):
    model = TrainingRegister()
    form = TrainingRegisterForm(request.POST,request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def register_edit(request, pk):
    model = TrainingRegister.objects.get(id=pk)
    form = TrainingRegisterForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client:product_list')
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/products/form.html', ctx)

@login_required_decorator
def register_delete(request, pk):
    model = TrainingRegister.objects.get(id=pk)
    model.delete()
    return redirect('client:product_list')
