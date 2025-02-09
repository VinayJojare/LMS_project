from django.urls import path, include
from .views import TeacherView, StudentView, ParentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teachers', TeacherView, basename='teachers')
router.register(r'students', StudentView, basename='students')
router.register(r'parents', ParentView, basename='parents' )
urlpatterns = [
    path('', include(router.urls))
]