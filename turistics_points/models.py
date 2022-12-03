from django.db import models
from equipments.models import Equipment

# Create your models here.
class TuristicPoint(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    approval = models.BooleanField(default=False)
    equipments = models.ManyToManyField(Equipment, related_name="Turistic_Point")
    
    def __str__(self) -> str:
        return self.name