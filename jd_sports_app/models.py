
from django.db import models

class Jersey(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='jersey_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.team})"