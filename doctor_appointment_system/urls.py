"""
doctor_appointment_system URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appointment.views import PatientListView

admin.site.site_header = "Alpha Health Admin"
admin.site.site_title = "Alpha Health Admin Portal"
admin.site.index_title = "Welcome to Alpha Health"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('appointment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
