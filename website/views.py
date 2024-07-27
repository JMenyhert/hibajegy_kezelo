from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Problem
from .forms import AddRecordForm



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
        return render(request, "home.html", {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "Kilpétél")
    return redirect("home")

def fault_record(request, pk):
    if request.user.is_authenticated:
        fault_record = Problem.objects.get(id=pk)
        return render(request, 'record.html', {'fault_record': fault_record})
    else:
        messages.success(request, "Be kell lépned, hogy láthasd!")
        return redirect("home")

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Problem.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Sikeresen törölted a hibajegyet!")
        return redirect("home")
    else:
        messages.success(request, "Be kell lépned, hogy láthasd!")
        return redirect("home")

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Sikeresen felvetél egy hibajegyet")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})

    else:
        messages.success(request, "Kérlek lépj be")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Problem.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Sikeresen módosítottad a hibajegyet")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Kérlek lépj be")
        return redirect('home')