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
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="Turistic_Point", null=True, blank=True) 
    localizations = models.ForeignKey(Localization, on_delete=models.CASCADE, related_name="Turustuc_Points", null=True, blank=True)   
    photo = models.ImageField(upload_to="point_turistic", null=True, blank=True)
    def __str__(self) -> str:
        return self.name

