from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('firstapp:home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'An Account has been made for ' + user)

				return redirect('firstapp:login')
			

		context = {'form':form}
		return render(request, 'firstapp/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('firstapp:home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('firstapp:home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'firstapp/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('firstapp:login')

@login_required(login_url='firstapp:login')
def home(request):
    context = {}
    return render(request, 'firstapp/home.html', context)

@login_required(login_url='firstapp:login')
def task(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('firstapp:task')

    context = {'tasks':tasks, 'form':form}

    return render(request, 'firstapp/task.html', context)

@login_required(login_url='firstapp:login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('firstapp:task')

    context = {'form':form}

    return render(request, 'firstapp/update_task.html', context)

@login_required(login_url='firstapp:login')
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('firstapp:task')

    context = {'item':item}

    return render(request, 'firstapp/delete_task.html', context)

@login_required(login_url='firstapp:login')
def status(request):
    
    tasks = Task.objects.all()

    context = {'tasks':tasks}

    return render(request, 'firstapp/status.html', context)

@login_required(login_url='firstapp:login')
def delete_all(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        tasks.delete()
        return redirect('firstapp:task')

    context = {'tasks':tasks}

    return render(request, 'firstapp/delete_all.html', context)

@login_required(login_url='firstapp:login')
def aboutUs(request):
    return render(request, 'firstapp/about.html')

@login_required(login_url='firstapp:login')
def Note(request, pk):

    item = Task.objects.get(id=pk)

    form = TaskForm(instance=item)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('firstapp:task')

    context = {'item':item, 'form':form}

    return render(request, 'firstapp/note.html', context)

@login_required(login_url='firstapp:login')
def priority(request):
    tasks = Task.objects.all()

    context = {'tasks':tasks}

    return render(request, 'firstapp/prior.html', context)


