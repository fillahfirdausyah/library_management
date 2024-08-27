from django.db import models

class Authors(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name
