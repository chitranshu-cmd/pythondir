from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views


routers = routers.DefaultRouter()
routers.register(r'students', views.StudentViewSet,basename='Student')

urlpatterns = [
    path('',include(routers.urls)),
    path('api_auth/',include('rest_framework.urls', namespace='rest_framework')),


]
