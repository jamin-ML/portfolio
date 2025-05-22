from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='projects/')
    urls = models.URLField(blank=False)

    def __str__(self):
        return self.title
    
class Ml_Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='projects/')
    urls = models.URLField(blank=False)

    def __str__(self):
        return self.title
    
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name

class TechIcon(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.name

class PageView(models.Model):
    page_name = models.CharField(max_length=100, unique=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.page_name} - {self.count} views"
