from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForms
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now login')
            return redirect('login')
    else:
        form = UserRegistrationForms(request.POST)
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')