from django.db import models

# Create your models here.
class Name(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 230)
    def __str__(self):
        return self.firstname

class Contact(models.Model):
    name= models.CharField(max_length=200)
    contactDetails = models.IntegerField()
    def __str__(self):
        return self.name
class Address(models.Model):
    name = models.ForeignKey(Name, on_delete = models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    firstaddress=models.CharField(max_length=200)
    secondaddress = models.CharField(max_length=200)

