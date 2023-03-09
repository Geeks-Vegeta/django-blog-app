from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    return render(request, "home.html", {"user":user})


def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out of Blog")
    return redirect('login')

@csrf_exempt
def registerUser(request):

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method=="POST":
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password=request.POST['confirm_password']
        if confirm_password!=password:
            messages.info("Password should be same as confirm password")
        try:
            user = User.objects.create_user(username, email, password);
            user.save()
            login(request, user)
            messages.success(request, "Logged In Successfully")
            return redirect("/")
        except IntegrityError:
            messages.info(request, "Try different Username")
            return render(request, "users/register.html")
        

    return render(request, "users/register.html")

@csrf_exempt
def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            user = authenticate(username=request.POST["name"], password=request.POST["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "Logged In Successfully")
                return redirect('/')
            else:
                messages.info(request, "No User Found")
        return render(request, "users/login.html")
    return redirect("/")
