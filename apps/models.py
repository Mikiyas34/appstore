from django.db import models
from account.models import User

class App(models.Model):
    owner = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=300)
    link = models.URLField()
    category_choices = [
        ("Education", "Education"),
        ("Entertainment", "Entertainment"),
        ("Finance", "Finance"),
    ] 
    category = models.CharField(choices=category_choices)
    points = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name