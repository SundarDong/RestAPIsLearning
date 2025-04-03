from django.db import models

# Create your models here.

class User(models.Model):  
    age = models.IntegerField()
    name = models.CharField(max_length=100)

#Yesle lew chai string ma return garne ho Mathi ko Model Ko user ko details lai 
def __str__(self):
        return self.name



