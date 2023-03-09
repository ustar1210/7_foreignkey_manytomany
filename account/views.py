from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserForm
# Create your views here.
def signin(request):
    if request.method == 'POST':
        usr = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=usr, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('post:index')
        else :
            return redirect('post:index')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = auth.authenticate(request, username=username, password=raw_password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('post:index')
                else :
                    return redirect('post:index')
        except:
            return redirect('post:index')

    else:
        return redirect('post:index')


def logout(request):
    auth.logout(request)
    return redirect('post:index')