from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
# Create your views here.



def Register(request):
    return render(request,"Authentication/Register.html")

def Login(request):
    return render(request, "Authentication/Login.html")


def customer_registration_form_submission(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken')
                return redirect("/Register")

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                auth.login(request, user)
                return redirect("/")
        else:
            messages.info(request, "Password did not match")
            return redirect("/Register")

    else:
        return redirect("/Register")

def customer_login_form_submission(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, 'User does not exist! please register')
            return redirect("/Login")

def About(request):
    return render(request, "Authentication/about.html")

def Logout(request):
    auth.logout(request)
    return redirect("/")