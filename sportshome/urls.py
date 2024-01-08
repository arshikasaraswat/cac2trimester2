from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('staff' ,views.staff),
    path('achievement', views.achievement)
]