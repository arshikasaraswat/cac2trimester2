from django.urls import path, include
from .views import *
urlpatterns = [
    path('', login_app, name='login'),
    path('staff', staff),
    path('achievement', achievement)
]
