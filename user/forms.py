
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback
 
 
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length = 20)
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.',
        error_messages={
            'unique': 'A user with this email address already exists.'
        }
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'first_name']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']