from django.db import models

# Create your models here.

class Software(models.Model):
    name = models.CharField(max_length=100)
    displayName = models.CharField(max_length=100,blank=True)
    logo = models.CharField(max_length=255,blank=True,default='')
    version = models.CharField(max_length=20,blank=True,default='')
    publisher = models.CharField(max_length=50,blank=True)
    description = models.TextField(blank=True,default='')
    detectionRules = models.JSONField(blank=True)
    returnCodes = models.JSONField(blank=True)
    installStr = models.CharField(max_length=255,blank=True)
    uninstallStr = models.CharField(max_length=255,blank=True)
    enabled = models.BooleanField(default=True)

def __str__(self):
    return "software:{}".format(self.name)