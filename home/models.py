from django.db import models

# Create your models here.
class Suggestion(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    vsug = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Query(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    comment= models.TextField()
    date = models.DateField()  
    def __str__(self):
        return self.name  

class Thoughts(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    thought= models.TextField()
    date = models.DateField() 
    def __str__(self):
        return self.name   

class Regngo(models.Model):
    name = models.CharField(max_length=122)
    pocname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    pincode =models.IntegerField()
    address= models.TextField()
    number = models.IntegerField()
    date = models.DateField() 
    def __str__(self):
        return self.name 

class Regres1(models.Model):
    name = models.CharField(max_length=122)
    pocname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    regnum = models.IntegerField()
    state = models.CharField(max_length=122)
    pincode =models.IntegerField()
    address= models.TextField()
    number = models.IntegerField()
    date = models.DateField() 
    def __str__(self):
        return self.name   

class Volunteer(models.Model):
    name = models.CharField(max_length=122)
    
    email = models.CharField(max_length=122)
    
    address= models.TextField()
    number = models.IntegerField()
    date = models.DateField() 
    def __str__(self):
        return self.name      