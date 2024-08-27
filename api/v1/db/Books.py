from django.db import models

class Books(models.Model):
    author = models.ForeignKey('Authors', on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateField()

    def __str__(self):
        return self.title