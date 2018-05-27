from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Pippo'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args )


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            #return redirect('/account')
            return render(request, 'accounts/home.html')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


def view_profile(request):
    args = {'user': request.user}
    return render(request,'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'accounts/profile.html')

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

