from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Problem



# Create your views here.
def home(request):
    records = Problem.objects.all()

    # Megnézni, hogy be van-e jelentkezve
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        # autentikáció
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Sikeresen beléptél!")
            return redirect("home")
        else:
            messages.success(request, "Valamit elgépeltél, próbáld újra ")
            return redirect("home")
    else:
        return render(request, "home.html", {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "Kilpétél")
    return redirect("home")