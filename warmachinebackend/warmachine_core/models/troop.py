from django.db import models

from warmachine_core.models.force import Force

class Troop(models.Model):
    name = models.CharField(max_length=255)

    type = models.CharField(max_length=255)
    
    level = models.PositiveSmallIntegerField()

    number = models.PositiveSmallIntegerField()

    ac = models.PositiveSmallIntegerField()
    
    abilities = models.CharField(max_length=255)
    
    spells = models.BooleanField()
   
    force = models.ForeignKey(Force, on_delete=models.PROTECT)
