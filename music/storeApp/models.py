from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    price = models.FloatField()
    albumImage = models.ImageField(upload_to='albumImages/', null=True, blank=True)

    def __str__(self):
        return self.name
    

