from django.db import models

# Create your models here.

TOBE_STATUS =(
    ('notstarted','notstarted'),
    ('inprogress','inprogress'),
    ('completed','completed'),
    
)

class Tobe(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    status = models.CharField(max_length=20,choices=TOBE_STATUS,default='notstarted')
    
    def __str__ (self):
        return self.name