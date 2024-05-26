from django.db import models

# Create your models here.
class Tag(models.model):
    name  = models.CharField(max_length=200, unique=True)
        
    def__str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)
    
    
    def __str__(self):
        return self.title
    
    