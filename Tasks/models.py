from django.db import models

# Create your models here.

class Tarea(models.Model):
    tarea_desc = models.CharField(max_length=200)
    def __str__(self):
        return self.tarea_desc