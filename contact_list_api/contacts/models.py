from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Contacts(models.Model):
    class Meta:
        verbose_name_plural = "Contacts"
        
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    contact_picture = models.URLField(null=True,blank=True)
    is_favourite =  models.BooleanField(default=True)

    def __str__(self):
        return self.first_name