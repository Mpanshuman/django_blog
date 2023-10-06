from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    form = UserRegisterForm()
    context = {"form": form}
    if request.method == "POST":
        pass
    return render(request, "user/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created")
            return redirect("blog-home")
    form = UserRegisterForm()
    context = {"form": form}

    return render(request, "user/register.html", context)

@login_required
def profile(request):
    return render(request, "user/profile.html")
