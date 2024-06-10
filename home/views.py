from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import User
from apps.models import App
from django.http import HttpResponse
def home(request):
    context = {
        'user_authenticated': request.user.is_authenticated,
        'user': request.user 
    }
    if request.user.is_authenticated:
        user = request.user
        if user.role == 'Admin':
            return render(request, 'admin.html', {'user': user})
        elif user.role == 'User':
            return render(request, 'user.html', {'user': user})
        else:
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)
    

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def tasks(request):
    if request.method == 'POST':
        appId = request.POST.get('app_id')
        app = App.objects.get(id=appId)
        user = request.user
        user.tasks.add(app)
        user.save()
        return HttpResponse("Task added")
    elif request.method == 'GET':    
        user = request.user
        user_tasks = user.tasks.all()
        return render(request, 'tasks.html', {'user_tasks': user_tasks})