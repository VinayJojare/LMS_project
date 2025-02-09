from django.urls import path, include
from .views import AttendanceView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'attendance', AttendanceView, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
]