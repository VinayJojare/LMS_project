from django.shortcuts import render 
from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, GetSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class GetUserView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = GetSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
# ------------------------------------------------------------------------------------

def get_data(request):
    return render(request, 'index.html')



