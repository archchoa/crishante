from django.db import models

from adminsortable.models import SortableMixin


class Section(SortableMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Photo(SortableMixin):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    section = models.ForeignKey('gallery.Section', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
