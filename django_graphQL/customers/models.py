from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

