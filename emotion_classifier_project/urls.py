from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from user import views
from django.contrib.auth import views as auth
from django.contrib.auth import views as auth_views


from rest_framework.authtoken import views
from user import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emotion_classifier_app/', include('emotion_classifier_app.urls')),

    path('', include('user.urls')),
    path('login/', user_view.login, name ='login'),
    path('register/', user_view.register, name ='register'),
    path('login/', user_view.logout_view, name='logout'),
    path('password-reset/', user_view.ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),


]
