from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from student.models import StudentProfile
from student.serializers import StudentProfileSerializer


# Create your views here.
class StudentProfileViewset(ModelViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()
