from django.db import models

# Create your models here.

class Emp(models.Model):
    name = models.CharField(max_length=30)
    email =models.EmailField()
    password =models.CharField(max_length=20)
    number =models.IntegerField()
    pCode = models.IntegerField()
    gender =models.CharField(max_length=30)
    address =models.CharField(max_length=300)
    hobbey =models.CharField(max_length=300)
    state =models.CharField(max_length=30)
    uname =models.CharField(max_length=10)
    dob = models.CharField(max_length=10)

class Blog(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    postby = models.CharField(max_length=30)

class Comment(models.Model):
    msg= models.CharField(max_length=300)
    cid=models.ForeignKey(Blog, models.CASCADE)
