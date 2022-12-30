from django.db import models
from django.utils import timezone
now = timezone.now()

# Create your models here.
class Catogery(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self) -> str:
        return self.name
class SubCatogery(models.Model):
    cat=models.ForeignKey(Catogery,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    mrp=models.IntegerField(default=10)

class AddData(models.Model):
    catogery=models.CharField(max_length=100)
    sub_catogery=models.CharField(max_length=100)
    mrp =models.IntegerField(default=10)
    quantity =models.IntegerField(default=1)
    total =models.IntegerField(default=1)
    date = models.DateTimeField(default=now)

