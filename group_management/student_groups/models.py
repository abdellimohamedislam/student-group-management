from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    n=models.CharField(max_length=50)
    numero_inscription = models.CharField(max_length=20)
    bac_year = models.CharField(max_length=50,default=2023)
    matricule = models.CharField(max_length=12, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    group_actual = models.CharField( max_length=150,default=0)

    def __str__(self):
        return f'{self.nom} {self.prenom} - {self.matricule}'
