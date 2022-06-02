from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request,"home.html")

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirmpassword=request.POST["confirmpassword"]
        # print(category)
        if(confirmpassword!=password):
            return HttpResponse("Password is not confirmed")
        user=User.objects.create_user(username,email,password,first_name=firstname,last_name=lastname)
        # User.user_permissions.
        user.save()
        return redirect("/register/")
    return render(request,"pages-register.html")

def handlelogin(request):
    if request.method=="POST":
        loginusername=request.POST["username"]
        loginpassword=request.POST["password"]
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            return redirect("/clgsite/")
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,"pages-login.html")

def handlelogout(request):
    logout(request)
    return redirect("/")