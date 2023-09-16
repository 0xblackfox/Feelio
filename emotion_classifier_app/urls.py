from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('text/', views.text, name='text'),
    path('image/', views.image, name='image'),
    path('video/', views.video, name='video'),
    path('video_feed_bangla', views.video_feed_bangla, name='video_feed_bangla'),
    path('video_feed_english', views.video_feed_english, name='video_feed_english'),
    path('music_recommendations/', views.music_recommendations, name='music_recommendations'),

]
