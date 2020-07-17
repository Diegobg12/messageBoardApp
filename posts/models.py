from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

    def title(self):
        title = self.text[:15] 
        return title
