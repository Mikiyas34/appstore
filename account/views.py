from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
        
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])  
            user.save() 
            return redirect('login')
        else:
            return render(request, "register.html", {'form': form})
        

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request,'login.html', {'form': form})
    
    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            print("user autenticated", user.username)
            return redirect('home')
        else: 
            print("user not autenticated")
            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("login")