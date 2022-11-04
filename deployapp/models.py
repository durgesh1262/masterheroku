from django.db import models

class DeployModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    
    def __str__(self):
        return self.name
    

# Create your models here.
