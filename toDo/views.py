from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "GET":
        return render(request, "register.html",{'form':UserCreationForm()})
