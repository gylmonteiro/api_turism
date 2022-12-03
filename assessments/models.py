from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Assessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    point = models.DecimalField(max_digits=2, decimal_places= 1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"User: {self.user} | Point: {self.point}"