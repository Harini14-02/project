from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import admin
from django.contrib.auth.models import User

# Create your views here.

    
def home3(request):
    return render(request,"app2/home3.html")
def user_login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        print(username1, password1)
        user = authenticate(request, username=username1, password=password1)
        print(user)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('admin/', admin.site.urls)
            else:
                login(request,user)
                return redirect('home')  
        else:
            msg = "Invalid Credentials. Please try again!"
            return render(request,"app2/home2.html", {'msg': msg})
    return render(request,"app2/home2.html")

def register(request):
    if request.method == 'POST':
        name = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['pass'].strip()

        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()
        # userDetails.objects.create(user=new_user,)
        return redirect('user_login')
    else:
        return render(request, 'app2/home3.html')