from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, GetUserView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='tokenrefresh'),
    path('getdata/', GetUserView.as_view(), name='getuser'),
    
]