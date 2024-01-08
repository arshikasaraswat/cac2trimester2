from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

def index(request):
    return render(request , 'student_module/student.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None and user.is_active:
            if user.is_superuser == False and user.is_staff == False:
                login(request , user)
                return render('index')
            else:
                msg = "You are not authorized for this login!"
                return render(request , 'login/login.html' , {'msg':msg})
        else:
            msg = "Wrong credentials!"
            return render(request , 'login/login.html' , {'msg':msg})


