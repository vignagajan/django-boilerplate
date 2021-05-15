from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgot/', auth_views.PasswordChangeView.as_view(), name='forgot'),
]