from django.db import models

# Create your models here.
class Calculation(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.expression} = {self.result}'