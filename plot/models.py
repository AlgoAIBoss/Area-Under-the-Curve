from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Plot(models.Model):
    method = models.ForeignKey('Methods', on_delete=models.PROTECT)
    function = models.CharField(max_length=100)
    start = models.IntegerField()
    end = models.IntegerField()
    split = models.IntegerField()

    def __str__(self):
        return self.method


class Methods(models.Model):
    method = models.CharField(max_length=100)

    def __str__(self):
        return self.method
