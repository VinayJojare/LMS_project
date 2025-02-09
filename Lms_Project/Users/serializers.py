from rest_framework import serializers
from .models import Teacher, Student, Parent

# Teacher Serializer:
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
# --------------------------------------
# Student Serializer :
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
# -----------------------------------------
# Parent Serializer:

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'



