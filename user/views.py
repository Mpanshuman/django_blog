from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def login(request):
    form = UserCreationForm()
    context = {
        'form':form
    }
    if request.method == 'POST':
        pass
    return render(request, "user/login.html",context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created')
        return redirect('blog-home')
    else:
        form = UserCreationForm()
        context = {
            'form':form
        }
        return render(request, "user/register.html",context)
    
