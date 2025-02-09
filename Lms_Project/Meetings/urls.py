from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeetingView

router = DefaultRouter()
router.register(r'meetings', MeetingView, basename='meetings')

urlpatterns = [
    path('', include(router.urls)),
]