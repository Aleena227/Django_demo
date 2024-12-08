from django.db import models

# Create your models here.
#model definition
class employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to="image")

    def __str__(self):
        return self.name
