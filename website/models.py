from django.db import models


# Create your models here.
class Problem(models.Model):
    letrehozva = models.DateTimeField(auto_now_add=True)
    leado_neve = models.CharField(max_length=50)
    hardware_vagy_szotver_hiba = models.CharField(max_length=50)
    rovid_leiras = models.CharField(max_length=300)
    prioritasa = models.CharField(max_length=30)

    def __str__(self):
        return (f"{self.leado_neve} {self.prioritasa}")


# Fontos a migration-t használni, mert így a django átalakítja a megfelelő kódra(sql stb.)
# python manage.py makemigrations (létre hozza a migrations mappaban a 00001_initial.py-t ebben az esetben)
# ezután python manage.py migrate (feltölti az adatbázisba)