from django.shortcuts import render 
from .models import LiveMeeting
from .serializers import MeetingSerialzier
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class MeetingView(ModelViewSet):
    queryset = LiveMeeting.objects.all()
    serializer_class = MeetingSerialzier
    # permission_classes = [IsAuthenticated]


