from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Task
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == "GET":
        return render(request, "register.html",{'form':UserCreationForm()})
    else:
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(username=request.POST.get(
                    'username'), password=request.POST.get('password2'))
            except IntegrityError:
                error = "This user already exists. Try again"
                return render(request, 'register.html', {'form': UserCreationForm(), 'error': error})
            else: #ten esle wykonuje się, kiedy dojdzie do skutku try = czyli nie wystąpi tam błąd
                user.save()
                login(request,user)
                return redirect('home')
        else:
            error = "Your passwords do not match"
            return render(request, 'register.html', {'form': UserCreationForm(), 'error': error})


def log(request):
    if request.method == "GET":
        return render(request, 'log.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    #authenticate zwraca obiekt usera (instancję klasy user) - w tym przypadku username i hasło, to się dzieje,
    # kiedy dane są poprawne, jeśli są niepoprawne to zwraca None.
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            log_error = "User name or password is not valid. Try again."
            return render(request, 'log.html', {'form': AuthenticationForm(), 'log_error': log_error})

def home(request):
    return render(request, 'home.html')


# def log_out(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect('home')

# w log in musimy przekazać i request i usera, ponieważ aplikacja musi widzieć, kogo loguje.
# w funkcji log_out nie musimy tego robić, ponieważ system już wie, kto jest zalogowany

@login_required
def log_out(request):
    logout(request)
    return redirect('home')

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user) #request.user to jest ten user, aktualnie zalogowany
    return render(request, 'tasks.html', {"tasks": tasks})







