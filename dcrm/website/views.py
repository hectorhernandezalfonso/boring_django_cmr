from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#30:06


# Create your views here.


def home(request):
    #check login

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # auth
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Succesfull')
            return redirect(home)
        
        else:
            messages.success(request, 'Wrong Login!')
            return redirect(home)
        
    
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success('You logout!')
    return redirect(home)

