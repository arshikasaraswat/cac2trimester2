from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'sportshome.html')

def login_app(request):
    return render(request,'login/login.html')

def staff(request):
    return render(request, 'staff.html')
def achievement(request):
    return HttpResponse('Sports Registration and achievements')

