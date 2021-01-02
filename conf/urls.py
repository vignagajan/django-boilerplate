from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
]
