from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views import View

        
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apps')
        else:
            return render(request, "register.html", {'form': form})
        