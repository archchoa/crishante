from django.db import models

from adminsortable.models import SortableMixin


class Portfolio(SortableMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    main_image = models.ImageField(upload_to='images')
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Work(SortableMixin):
    header = models.CharField(max_length=255, blank=True)
    subheader = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    portfolio = models.ForeignKey(
        'portfolio.Portfolio', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.header


class Photo(SortableMixin):
    image = models.ImageField(upload_to='images')
    work = models.ForeignKey(
        'portfolio.Work', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.image.url
