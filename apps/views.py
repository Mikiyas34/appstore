from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import App
from django.contrib.auth.decorators import login_required


@login_required
def get_apps(request):
    user = request.user
    if user.role == 'Admin':
        return redirect('/')
    else: 
        apps = App.objects.all()
        return render(request, 'apps.html', {'apps': apps})


def get_app(request, id):
    app = get_object_or_404(App, id=id)
    return render(request, "app_detail.html", {'app': app})

@login_required
def create_app(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('appname')
        link = request.POST.get('applink')
        image = request.FILES.get('appimage')
        category = request.POST.get('category')
        points = request.POST.get('points')
        print(request.FILES)
        if name and link and image and category and points:
            app = App.objects.create(
                owner=user,
                name=name,
                link=link,
                image=image,
                category=category,
                points=points
            )
            app.save()
            return redirect('/')
        else: 
            context = {
                'error': 'All fields are required.',
                'appname': name,
                'applink': link,
                'category': category,
                'points': points
            }
            return render(request, 'create_app.html', context)
        
    elif request.method == 'GET':
        return render(request, "create_app.html")
