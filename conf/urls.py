from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView,RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('favicon.ico',RedirectView.as_view(url=staticfiles_storage.url('/images/favicon.ico'))),
    path('admin/', admin.site.urls),
    path('privacy/', TemplateView.as_view(template_name='privacy-policy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='terms-of-use.html'), name='terms'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('apps.users.urls')),

]
