from django.db import models

# Create your models here.
# models.py
from django.db import models

class Depo(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    transport_count = models.IntegerField()

class Driver(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Transport(models.Model):
    depo = models.ForeignKey(Depo, on_delete=models.CASCADE)
    route_number = models.IntegerField()
    transport_type = models.CharField(max_length=200)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

class Trolleybus(models.Model):
    number = models.IntegerField()
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    image = models.ImageField(upload_to='trolleybus_images')
