from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250,default ="")
    content = models.TextField()
    author = models.CharField(max_length=50,default ="")
    slug = models.CharField(max_length=130,default ="")
    views = models.IntegerField(default=0)
    timestump = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

class blogs_comment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    posts = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null= True)
    timestump = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.comment[:8]} by {self.user.username}'
    
