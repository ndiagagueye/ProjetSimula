from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth import login as auth_login
from django.db.models import Q
from .models import *
from .forms import *


def login(request):
    error = False
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            dj_login(request, user)
            error = False
            if request.GET.get('next', False):
                return redirect(request.GET['next'])
            else:
                return redirect("/")
        else:
            error = True
    return render(request, 'users/login.html', locals())


def register(request):
    form = RegisterForm(request.POST or None)
    username_error = password_error = password_length_error = False
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        password_confirm = form.cleaned_data['password_confirm']
        if len(password) < 6:
            password_length_error = True
        elif password != password_confirm:
            password_error = True
        else:
            users = User.objects.all()
            for user in users:
                if user.username == email:
                    username_error = True
            if not username_error:
                new_user = User.objects.create_user(email,  email, password)
                new_user.name = name
                user = Users()
                user.user = new_user
                user.name = name
                user.save()

                new_user = authenticate(email=user.username, password=password)

                dj_login(request, new_user)
    return render(request, 'users/register.html', locals())


def profile(request):
    error = False
    if request.method == ["POST"]:
        profession = request.POST['select-profession']
        # if profession == "" :

        if profession == "Professeur" or profession == "Eleve" or profession == "Etudiant" or profession == "Docteur" or profession == "Enseignant chercher":

            error = False
            prof = User.objects.get(id=3)
            prof.value = profession
            prof.save
        else:

            error = True


    else:

        error = False

    return render(request, 'users/profile.html', locals())
