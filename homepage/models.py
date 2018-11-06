from django.db import models

from adminsortable.models import SortableMixin


class Slide(SortableMixin):
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.image.url


class Testimonial(SortableMixin):
    customer = models.CharField(max_length=255)
    text = models.TextField()
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.customer
