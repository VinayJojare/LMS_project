from django.contrib import admin
from django.urls import path, include
from LMS.views import get_data
from Assignments.views import assignment_operations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('LMS.urls')),
    path('api/', include('Users.urls')),
    path('api/', include('Assignments.urls')),
    path('api/', include('Notes.urls')),
    path('api/', include('Attendance.urls')),
    path('api/', include('Meetings.urls')),
    path('get_data/', get_data, name='get_data'),
    path('assignments/', assignment_operations, name='assignments'),
]
