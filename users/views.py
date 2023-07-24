from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CreateUser
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist try to <strong><a href={% url "user_register" %}>Register</a></strong>')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome Back !!!')
            return redirect('base:dashboard')
        else:
            messages.error(request, 'Votre nom d\'utilisateur ou bien votre mot de passe ne sont pas correct!')
    return render(request, 'users/user_login.html' )

def user_logout(request):
    logout(request)
    return redirect('base:dashboard')

def user_register(request):
    form = CreateUser()
    if request.method == 'POST':
        #if User.objects.get(username=request.POST['username']) :
        #    messages.error(request,'This Username is already taken !!!')
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, f'Your account <strong>"{user.username}"</strong> was created successfully !!!')
            return redirect('base:home')
        else:
            username = request.POST['username']
            if User.objects.get(username=username):
                messages.error(request, 'This user is already exist !!! ')
            if form['password2'].errors:
                messages.error(request, 'The two password fields didn\'t match.')
            
    context = {
        'form':form,
    }
    return render(request, 'users/user_register.html', context)

