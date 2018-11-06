from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    section = models.ForeignKey('gallery.Section', on_delete=models.CASCADE)
