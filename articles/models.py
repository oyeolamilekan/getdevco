from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=True)
    objects = models.Manager()
    topic = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return f'{self.topic} {self.body}'
