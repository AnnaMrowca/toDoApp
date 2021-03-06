"""toDoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from toDo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register, name="register"),
    path('log', views.log, name="log"),
    path('', views.home, name="home"),
    path('logout', views.log_out, name="logout"),
    path('tasks', views.tasks, name="tasks"),
    path('create', views.create, name="create"),
    path('tasks/<int:taskId>/edit', views.edit, name="edit"),
    path('tasks/<int:taskId>/delete', views.delete_task, name="delete_task"),
    path('tasks/<int:taskId>/complete', views.complete_task, name="complete_task"),

]
