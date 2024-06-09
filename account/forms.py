from django.forms import ModelForm, CharField, PasswordInput, Select, ValidationError
from .models import User



class RegisterForm(ModelForm):
     password = CharField(widget=PasswordInput)
     password_confirm = CharField(widget=PasswordInput)
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
         
     def clean(self):
         cleaned_data = super().clean()

         password = cleaned_data['password']
         password_confirm = cleaned_data['password_confirm']

         if password and password_confirm and password_confirm != password:
               raise ValidationError("Passwords don't match")
         
         return cleaned_data

