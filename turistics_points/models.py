from django.db import models
from equipments.models import Equipment
from comments.models import Comment
from localizations.models import Localization
# Create your models here.
class TuristicPoint(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    approval = models.BooleanField(default=False)
    equipments = models.ManyToManyField(Equipment, related_name="Turistic_Point", blank=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="Turistic_Point") 
    localizations = models.ForeignKey(Localization, on_delete=models.CASCADE, related_name="Turustuc_Points")   
    
    def __str__(self) -> str:
        return self.name

