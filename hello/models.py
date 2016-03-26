from django.db import models

# Create your models here.


class Device(models.Model):
    device_id = models.CharField(max_length=128)
    device_name = models.CharField(max_length=128)


class Menu(models.Model):
    item_id = models.CharField(max_length=16)
    option_id = models.CharField(max_length=16)


class Log(models.Model):
    log_type = models.CharField(max_length=10)
    currenttime = models.DateTimeField()
    elapsedseconds = models.CharField(max_length=10)
    uxtimeremaining = models.CharField(max_length=10)
    orbactive = models.CharField(max_length=5)
    temp = models.FloatField()
    tempslope60 = models.IntegerField()
    currentorbits = models.FloatField()
    percentagecomplete = models.FloatField()
    estimatedremainingtime = models.CharField(max_length=10)
    deviceremainingtime = models.CharField(max_length=10)
    devicesynctime = models.CharField(max_length=10)
    devicetemp = models.FloatField()
    devicetempsynctime = models.IntegerField()
    deviceorbits = models.FloatField()
    deviceorbitssynctime = models.IntegerField()
    deviceslope60 = models.IntegerField()
    deviceslope60synctime = models.IntegerField()
