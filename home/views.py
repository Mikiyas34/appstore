from django.shortcuts import render


def home(request):
    context = {
        'user_authenticated': request.user.is_authenticated,
        'user': request.user 
    }
    return render(request, 'index.html', context)