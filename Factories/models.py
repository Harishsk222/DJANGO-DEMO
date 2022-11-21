from django.db import models


#Tables for Banglore Outlet
class Banglore(models.Model):    
    Date = models.DateField()
    Bl1 = models.IntegerField(default=0) 
    Bl2 = models.IntegerField(default=0)    
    Bl3 = models.IntegerField(default=0)    
    Bl4 = models.IntegerField(default=0)    
    Bl5 = models.IntegerField(default=0)    

 
def __str__(self):
        return self.Date

# Create your models  for MUMBAI here.
#_______________________________________________________________________
class Mumbai(models.Model):    
    Date = models.DateField()
    Ml1 = models.IntegerField(default=0) 
    Ml2 = models.IntegerField(default=0)    
    Ml3 = models.IntegerField(default=0)    
    Ml4 = models.IntegerField(default=0)    
    

 
def __str__(self):
        return self.Date


# Create your models  for MUMBAI here.
#_______________________________________________________________________

class Chennai(models.Model):    
    Date = models.DateField()
    Cl1 = models.IntegerField(default=0) 
    Cl2 = models.IntegerField(default=0)    
    Cl3 = models.IntegerField(default=0)    
      
    

 
def __str__(self):
        return self.Date