from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfilePicUpdateForm
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
    user_update_form = UserUpdateForm(instance=request.user)
    profile_update_form = ProfilePicUpdateForm(instance=request.user.profile)
    context = {
        'user_form':user_update_form,
        'profile_pic_form':profile_update_form,
    }

    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfilePicUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid():
            user_update_form.save()
        if profile_update_form.is_valid():
            profile_update_form.save()
        messages.success(request,"Account Updated")
        return redirect("user-profile")
    return render(request, "user/profile.html",context)
