from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('privacy/', TemplateView.as_view(template_name='privacy-policy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='terms-of-use.html'), name='terms'),
    path('', include('apps.users.urls')),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
]
