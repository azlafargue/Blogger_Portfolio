from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_lenght=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default = 0)
    