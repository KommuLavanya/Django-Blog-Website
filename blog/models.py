from django.db import models

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=50)
    content = models.TextField()
    timeStamp = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title + '-' + self.author
