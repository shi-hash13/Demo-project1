from django.db import models

# Create your models here.
class contact(models.Model):
   name = models.CharField(max_length=25,null=True)
   email = models.EmailField(max_length=50,null=True)
   mssg= models.CharField(max_length=100,null=True)
   delete_flag = models.BooleanField(default=False)

class PGRegister(models.Model):
    pg_name = models.CharField(max_length=50,null=True)
    pg_loaction = models.CharField(max_length=50,null=True)
    pg_type = models.CharField(max_length=50,null=True)
    pg_email = models.EmailField(max_length=50,null=True)
    pg_phone = models.BigIntegerField(null=True)
    room_type = models.CharField(max_length=50,null=True)
    meals = models.CharField(max_length=50,null=True)
    ac_room = models.CharField(max_length=50,null=True)
    laundary = models.CharField(max_length=50,null=True)
    furnish = models.CharField(max_length=50,null=True)
    wifi = models.CharField(max_length=50,null=True)
    m_rent = models.BigIntegerField(null=True)
    s_amount = models.BigIntegerField(null=True)
    a_charge = models.BigIntegerField(null=True)
    o_name = models.CharField(max_length=50,null=True)
    o_phone = models.BigIntegerField(null=True)
    o_address = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=500,null=True)
    image = models.FileField(upload_to='media/images/',null=True)
    rule = models.FileField(upload_to='media/images/',null=True)
    document = models.FileField(upload_to='media/images/',null=True)
    delete_flag = models.BooleanField(default=False)  

class UserCredentials(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)