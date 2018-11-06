from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    main_image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.title


class Work(models.Model):
    header = models.CharField(max_length=255, blank=True)
    subheader = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    portfolio = models.ForeignKey(
        'portfolio.Portfolio', on_delete=models.CASCADE)


class Photo(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    work = models.ForeignKey(
        'portfolio.Work', on_delete=models.CASCADE)
