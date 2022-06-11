from django.db import models

# Create your models here.
class student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.FileField()
    def __str__(self):
        return self.name

class emply(models.Model):
    reg = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary=models.IntegerField()
class register(models.Model):
    rol = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
class login(models.Model):
    use = models.CharField(max_length=50)
    pswd = models.CharField(max_length=50)

