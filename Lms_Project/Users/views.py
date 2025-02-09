from django.shortcuts import render 
from rest_framework.viewsets import ModelViewSet
from .serializers import TeacherSerializer, StudentSerializer, ParentSerializer
from .models import Teacher, Student, Parent
from rest_framework.permissions import IsAuthenticated

class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsAuthenticated]
# ------------------------------------------
# Student View:
class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]


class ParentView(ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer



