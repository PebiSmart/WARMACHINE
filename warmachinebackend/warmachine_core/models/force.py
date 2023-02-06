from django.db import models

from warmachine_core.models.leader import Leader

class Force(models.Model):
    name = models.CharField(max_length=255)
    
    affiliation = models.CharField(max_length=255, blank=True)
    
    leader = models.OneToOneField(Leader, on_delete=models.PROTECT)

    basic_force_rating = models.PositiveSmallIntegerField()