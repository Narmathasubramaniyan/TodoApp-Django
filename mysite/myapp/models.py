from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    category = models.CharField(max_length=100, null=True, blank=True)  
    estimate_time = models.CharField(max_length=50, null=True, blank=True)  
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
