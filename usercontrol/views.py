from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
# Create your views here.

def login_view(request, *args, **kwargs):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        print(username,password)

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'usercontrol/login.html', {'error': "Username and Password do not match."})
    else:
        return render(request, 'usercontrol/login.html', {})


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        emailaddress = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            return render(request, 'usercontrol/register.html', {'error':'This username is already taken'})
        if User.objects.filter(email=emailaddress).exists():
            return render(request, 'usercontrol/register.html', {'error':'This E-Mail is already taken.'})
                
            

        if password2 != password1:
            return render(request, 'usercontrol/register.html', {'error':'Passwords do not match'})
        
        user = User.objects.create_user(username=username, password=password1, email=emailaddress)
        user.save()

        print("Freakiinnnnn Finallyyyyyyyyyyyyyyyyyyyy")
        return redirect('/accounts/success')
        print(request.POST)
    else:
        return render(request, 'usercontrol/register.html', {})


def register_success_view(request, *args, **kwargs):
    
    return render(request, 'usercontrol/success.html', {})

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('/')