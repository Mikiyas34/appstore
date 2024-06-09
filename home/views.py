from django.shortcuts import render


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
    

