from django.db import models
from time import timezone

# Create your models here.
class SubmittedData(models.Model):
    candidate = models.CharField(max_length=40,null=True)
    time=models.CharField(max_length=100,null=True)
    list=models.CharField(max_length=300,null=True)

    
    def __str__(self):       
        return self.candidate +" time taken: "+ self.time+" ==>> "+ self.list