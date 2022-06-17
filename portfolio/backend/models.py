from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=999)
    subtitle = models.CharField(max_length=999)
    content = models.TextField()
    url = models.URLField(max_length=999)
    imgUrl = models.URLField(max_length=999)
    bgUrl = models.URLField(max_length=999)
    imgAlt = models.CharField(max_length=999)
    
    
    def __str__(self):
        return f"{self.title}"