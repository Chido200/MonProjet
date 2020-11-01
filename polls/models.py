from django.db import models

# Create your models here.
class Person(models.Model):
    nom = models.CharField(max_length=30)
    prenon = models.CharField(max_length=30, blank=False)
    /*def __str__(self):
        return f'{self.nom}  {self.prenon}'*/



