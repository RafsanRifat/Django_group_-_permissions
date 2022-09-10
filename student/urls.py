from django.urls import path
from rest_framework import routers
from .views import StudentProfileViewset

router = routers.SimpleRouter()

router.register(r'StudentProfile', StudentProfileViewset)