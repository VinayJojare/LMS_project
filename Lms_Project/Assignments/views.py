from django.shortcuts import render
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, SubmissionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from Lms_Project.permissions import IsTeacher


class AssignmentView(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    # Require authentication and teacher role
    # permission_classes = [IsAuthenticated, IsTeacher]

    def get_serializer_context(self):
        # Pass the request object to the serializer context
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

# Submission View:


class SubmissionView(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    # permission_classes = [IsAuthenticated]


def assignment_operations(request):
   
    return render(request, 'assignment.html')
