from django.urls import path
from .views import login, signup, home, logout, ProfileView, profile
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/logout/', logout, name='logout'),
    path('profile', profile, name='profile'),
]
