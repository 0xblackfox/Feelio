from django.contrib import admin
from .models import Feedback, UserProfile

admin.site.register(UserProfile)
admin.site.register(Feedback)
