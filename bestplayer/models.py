from django.db import models

class Club(models.Model):
    name = models.CharField(max_length = 40)
    created_date = models.DateField()
    premier = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.name
    
class Footballer(models.Model):
    club = models.ForeignKey(Club)
    name = models.CharField(max_length=60)
    amplua = models.CharField(max_length=30)
    number = models.IntegerField(default = 0)
    birth_date = models.DateField()
    #votes = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.name
    

    
