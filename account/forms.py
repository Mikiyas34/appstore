from django.forms import ModelForm, CharField, PasswordInput, Select
from .models import User


class RegisterForm(ModelForm):
     password = CharField(widget=PasswordInput)
     class Meta:
         model = User
         fields = ["username", "password", "role"]
         labels = {
            "username": "Username",  
            "password": "Password",
            "role": "Role"
            }
         widgets = {
            "role": Select(choices=User.ROLE_CHOICES)  
        }

