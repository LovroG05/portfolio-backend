from django.urls import path

from . import views



urlpatterns = [
    path('getprojects/', views.getProjects, name='getprojects'),
]