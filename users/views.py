from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PasswordReset
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse

# Create your views here.

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance= request.user)
        p_form = ProfileUpdateForm(request.POST , request.FILES, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated')
            return redirect('profile') 
    else:
        if request.user.is_authenticated:
            u_form = UserUpdateForm(instance = request.user)
            try:
                p_form = ProfileUpdateForm(instance = request.user.profile)
            except:
                logged_user = User.objects.get(id=request.user.id)
                save_profile_model = Profile(user=logged_user)
                save_profile_model.save()
                return redirect('profile')
            context ={
            'title' : 'profile',
            'u_form' : u_form,
            'p_form' : p_form
            }
            return render(request, 'users/profile.html', context)
        else:
            return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request,'users/register.html', context)

def password_reset(request):
    if request.method == 'POST':
        return redirect('password_reset_done')
    form = PasswordReset()
    context = {
        'form' : form
    }
    return render(request, 'users/password_reset.html', context)

def password_reset_done(request):
    return render(request, 'users/password_reset_done.html')