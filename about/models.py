from django.db import models

from adminsortable.models import SortableMixin


class TeamMember(SortableMixin):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Service(SortableMixin):
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
