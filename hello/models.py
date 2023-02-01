from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=1000, default="Kamudello")
    
    def __str__(self):
        return self.name
    
    