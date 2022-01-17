from django.db import models

class trainee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length = 10)
    salary = models.IntegerField(max_length = 10)

    def __str__(self) -> str:
        return self.name
