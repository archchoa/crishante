from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)


class Service(models.Model):
    name = models.CharField(max_length=255)
