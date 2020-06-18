from django.urls import path
from users.views import profile, register, password_reset, password_reset_done
from django.contrib.auth import views as auth_view
# Urls

urlpatterns = [
    path('', profile, name='profile'),
    path('register/',register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', password_reset, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
]
