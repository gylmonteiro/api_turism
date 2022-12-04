from django.db import models

# Create your models here.
class Localization(models.Model):
    public_place = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    coordenates_latitude = models.CharField(max_length=150, blank = True, null= True)
    coordenates_longitude = models.CharField(max_length=150, blank = True, null= True)

    def __str__(self) -> str:
        return self.public_place