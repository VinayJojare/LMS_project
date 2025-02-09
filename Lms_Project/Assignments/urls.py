from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import AssignmentView, SubmissionView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'assignments', AssignmentView, basename='assignments')
router.register(r'submissions', SubmissionView, basename='submissions')

urlpatterns = [
    path('', include(router.urls) ),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
