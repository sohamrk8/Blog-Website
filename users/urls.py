from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('sign_up',views.sign_up,name= 'sign_up'),
    path('profile/',views.profile_view ,name= 'user-profile'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'),name='users-login'),
    path('logout/',TemplateView.as_view(template_name='users/logout.html'),name='users-logout'),
    #forget password steps>>>>>>>>>>>>>
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name ='users/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name ='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name ='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name ='users/password_reset_complete.html'), name='password_reset_complete'),
]
