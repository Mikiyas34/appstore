from django.db import models
from account.models import User

class App(models.Model):
    owner = models.ForeignKey(User, models.CASCADE, verbose_name="Owner")
    name = models.CharField(max_length=300, blank=False, null=False)
    link = models.URLField(blank=False, null=False)
    image = models.ImageField(upload_to="uploads")
    category_choices = [
        ("Education", "Education"),
        ("Entertainment", "Entertainment"),
        ("Finance", "Finance"),
    ] 
    category = models.CharField(choices=category_choices, max_length=50, blank=False, null=False)
    points = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    

