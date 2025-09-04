from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {'form': form})


def login(request):
    return auth_views.LoginView.as_view(template_name='registration/login.html')


def logout(request):
    return auth_views.LogoutView.as_view(template_name='registration/logout.html')
