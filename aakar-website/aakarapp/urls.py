from django.urls import path,include
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import redirect_view


urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('dashboard', views.dashboard, name="dashboard"),
    path('updateProfile', views.updateProfile, name="updateProfile")
]
