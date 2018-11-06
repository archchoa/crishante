from django.db import models


class Slide(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')


class Testimonial(models.Model):
    customer = models.CharField(max_length=255)
    text = models.TextField()
