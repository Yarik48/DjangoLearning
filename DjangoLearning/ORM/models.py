from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Boock(models.Model):
    name = models.TextField(max_length=100)
    descriprition = models.CharField(max_length=1000)
    boock_pic = models.ImageField(upload_to='profile_pictures/')
    boock = models.FileField()
    reting = models.IntegerField()
    saved = models.ManyToManyField(User)
    catigoris = models.ForeignKey('Catigoris',on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('boock', kwargs={'boock_id' : self.pk})
class Catigoris(models.Model):
    name = models.TextField(max_length=33)