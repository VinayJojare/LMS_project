from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteView

router = DefaultRouter()
router.register(r'notes', NoteView, basename='notes')

urlpatterns = [
    path('', include(router.urls))
]