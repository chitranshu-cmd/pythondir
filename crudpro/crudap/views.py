from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
#from . models import DRFPost
from rest_framework import permissions

class StudentViewSet(viewsets.ModelViewSet):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer
      permission_classes = [permissions.IsAuthenticated]
# Create your views here.'''
