from django.db import models

# Create your models here.
class Item(models.Model):
    
    name = models.CharField(max_length=30, blank=False)  # text based input i.e. strings stored there. Blank means field can't be nullable (can't be left empty)
    done = models.BooleanField(blank=False, default=False) 


    def __str__(self): 
        return self.name 
        # dunder that returns the name of the instance of the object instead of the type (i.e. more readable for humans reviewing admin panel)