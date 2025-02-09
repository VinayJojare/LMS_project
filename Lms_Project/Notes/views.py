from django.shortcuts import render 
from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerialzier
from .models import Note
from rest_framework.permissions import IsAuthenticated

class NoteView(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerialzier
    # permission_classes = [IsAuthenticated]



