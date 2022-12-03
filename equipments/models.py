from django.db import models

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    opening_hours = models.TextField()
    approval = models.BooleanField(default=True)
    minimun_age = models.IntegerField()

    def __str__(self) -> str:
        return self.name