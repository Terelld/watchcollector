from django.db import models
from django.urls import reverse

SERVICE_TYPE = (
    ('R', 'Repair'),
    ('M', 'Maintenance'),
)




# Create your models here.
class Watch(models.Model): 
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    band_material = models.CharField(max_length=20)
    interface = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'{self.brand} - {self.model} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'watch_id': self.id})
    

class Service(models.Model):
    date = models.DateField('service date')
    service_type = models.CharField(
        max_length=1,
        choices=SERVICE_TYPE,
        default=SERVICE_TYPE[0][0]
    ) 
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_service_type_display()} on {self.date}'
