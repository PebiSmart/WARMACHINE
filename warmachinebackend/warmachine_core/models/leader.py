from django.db import models

class Leader (models.Model):
    name = models.CharField(max_length=255)
    
    level = models.PositiveSmallIntegerField()
    
    int_bonus = models.SmallIntegerField()
    
    wis_bonus = models.SmallIntegerField()
    
    cha_bonus = models.SmallIntegerField()
  
