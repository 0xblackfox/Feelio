
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
 
urlpatterns = [
        path('', views.login, name ='login'),
        path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  views.activate, name='activate'),
        path('feedback/', views.submit_feedback, name='submit_feedback'), 
        path('home/', views.protected_view, name='protected_view'),
        path('/', views.logout_view, name='logout'),

]