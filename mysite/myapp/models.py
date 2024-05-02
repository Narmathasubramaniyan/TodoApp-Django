from django.db import models

# Create your models here.
class Task(models.Model):


    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    category = models.CharField(max_length=100, null=True, blank=True)  
    estimate_time = models.CharField(max_length=50, null=True, blank=True)  
    end_date = models.DateField(null=True, blank=True)

   
