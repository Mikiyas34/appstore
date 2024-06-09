from django.forms import ModelForm
from .models import App


class CreateAppForm(ModelForm):
    class Meta:
        model = App
        fields = '__all__'

