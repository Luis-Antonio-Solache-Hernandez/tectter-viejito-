from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='')
    birth_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=50)
    public = models.BooleanField()
    biography = models.TextField(max_length=50)
    friend = models.Many_to_ManyField('self', blank=True)


class Tweet(models.MOdel):
    name = models.ForeignKey("Perfil", related_name='tweet')
    status = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
