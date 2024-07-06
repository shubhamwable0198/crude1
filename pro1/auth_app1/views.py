from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signview(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "auth_app1/sign.html", {"form": form})


def loginview(request):
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")

        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            return redirect("show")


    return render(request, "auth_app1/login.html", {})


def logoutview(request):
    logout(request)
    return redirect("login")