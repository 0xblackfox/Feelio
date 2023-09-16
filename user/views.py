from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib.auth.forms import AuthenticationForm
from user.models import UserProfile
from .forms import UserRegisterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.urls import reverse
from django.utils.encoding import force_bytes
from .forms import FeedbackForm
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'user/login.html', {'title':'login'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  
            user.save()
            # Activation token
            token = default_token_generator.make_token(user)

            UserProfile.objects.create(
                user=user,
                phone_no=form.cleaned_data['phone_no'],
                first_name=form.cleaned_data['first_name'],
               
            )
            current_site = get_current_site(request)
            subject = 'Activate your account'
            activation_link = request.build_absolute_uri(reverse("activate", args=[urlsafe_base64_encode(force_bytes(user.pk)), token]))
            message = f'Click the following link to activate your account: {current_site}{activation_link}'
            from_email = 'your_email@gmail.com'
            to = user.email

            msg = EmailMultiAlternatives(subject, message, from_email, [to])

            htmly = get_template('user/email.html')
            context = {'username': user.username, 'activation_link': activation_link}
            html_content = htmly.render(context)
            msg.attach_alternative(html_content, "text/html")

            msg.send()

            messages.success(request, 'An activation link has been sent to your email. Please activate your account.')
            return redirect('login')  
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'Register Here'})



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account has been activated! You can now log in.')
            return redirect('login')  
        else:
            messages.error(request, 'Invalid activation link. Please contact support.')
            return redirect('login')  
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    return HttpResponse('Activation link is invalid!')



@login_required  # Protect this view using the @login_required decorator
def protected_view(request):

    return render(request, 'emotion_classifier_app/home.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('protected_view') 
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form, 'title': 'Log In'})


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emotion_classifier_app/') 
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('')  



from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'user/password_reset.html'
    email_template_name = 'user/password_reset_email.html'
    subject_template_name = 'user/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')