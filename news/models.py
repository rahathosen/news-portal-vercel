from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title



  