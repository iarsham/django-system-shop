from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import CustomUser
from django.http import HttpResponse
from django.contrib import messages
# Verification Tools
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes


def auth_signup(request):
    auth_form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=info['username'], first_name=info['first_name'], last_name=info['last_name'],
                email=info['email'].lower(), phone_number=info['phone_number'], age=info['age'],
                password=info['password']
            )
            # Activation User
            current_site = get_current_site(request)
            subject = 'Please Active Your Account'
            message = render_to_string('registration/verification_mail.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_mail = user.email
            send_email = EmailMessage(subject, message, to=[to_mail])
            send_email.send()
            messages.success(request, 'The Activation Email Has Been Sent Please Check Your Inbox!')
            return redirect('login')
        else:
            messages.warning(request, " Please fill out Correctly All Forms !")
            return redirect('signup')

    context = {
        'form': auth_form,
    }
    return render(request, 'registration/signup.html', context)


def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login is Successfuly')
            return redirect('home')
        else:
            messages.warning(request, 'Username Or Password Is Not Correct!')
            return redirect('login')
    return render(request, 'registration/login.html')


def auth_logout(request):
    logout(request)
    return redirect('home')


def auth_activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except(ValueError, OverflowError, TypeError, CustomUser.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'You Account is Active , Login Now !')
        return redirect('login')
    else:
        messages.warning(request, 'this link is incorrect or expired')
        return redirect('signup')


# Reset Password
def forget_password(request):
    if request.method == "POST":
        email = request.POST['email'].lower()
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email__exact=email)
            # Reset Password Email
            current_site = get_current_site(request)
            mail_subject = "Reset Your Password"
            message = render_to_string('registration/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_mail = EmailMessage(mail_subject, message, to=[to_email])
            send_mail.send()
            messages.success(request, 'Link For Reset Your Passowrd Has Been Sent Check You Inbox')
            return redirect('home')
        else:
            messages.warning(request, 'Please enter the email with which you registered')
            return redirect('reset_mail')

    return render(request, 'registration/password_email_done.html')


def resetpassword_validate(request, uidb64, token):
    uid = None
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, OverflowError, ValueError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        return redirect('password_reset')
    else:
        messages.warning(request, 'Link is Incorrect or Expired!')
        return redirect('reset_mail')


def password_reset(request):
    if request.method == "POST":
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = CustomUser.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password Was Changed , Login With New Password!')
            return redirect('login')
        else:
            messages.warning(request, 'Password Format is incorrect or Not Same!')
            return redirect('password_reset')
    return render(request, 'registration/password_reset.html')
