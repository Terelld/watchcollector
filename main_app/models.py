from django.db import models



INTERFACE_CHOICES = [
    ('digital', 'Digital'),
    ('analog', 'Analog'),
]

# Create your models here.
class Watch(models.Model): 
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    band_material = models.CharField(max_length=20)
    interface = models.CharField(max_length=10, choices=INTERFACE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return f'{self.brand} - {self.model}'
