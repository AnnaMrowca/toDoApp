from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def register(request):
    if request.method == "GET":
        return render(request, "register.html",{'form':UserCreationForm()})
    else:
        if request.POST.get('password1') == request.POST.get('password2'):
            user =User.objects.create_user(username=request.POST.get(
                'username'), password=request.POST.get('password2'))
            user.save()
            return redirect('register')
        else:
            error = "Your passwords do not match"
            return render(request, 'register.html', {'form': UserCreationForm(), 'error': error})




