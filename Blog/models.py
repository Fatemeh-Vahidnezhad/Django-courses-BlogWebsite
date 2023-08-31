from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class blogs(models.Model):
    STATUS_CHOICE = (
        ('POP','Published'),
        ('DRF','draft'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view', args=[self.id])   # /blog/id/ --> /blog/5/ -->showing a url of a detail view of a post



