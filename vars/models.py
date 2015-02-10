from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=25, unique=True)
    active = models.BooleanField(default=True)
    model = models.CharField(max_length=10)
    address = models.CharField(max_length=16)
    description = models.CharField(max_length=255, blank=True)


class Var(models.Model):
    TYPE_CHOCES = (
        ('binary', "Binary"),
        ('real', "Real"),
    )
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=25, unique=True)
    active = models.BooleanField(default=True)
    device = models.ForeignKey(Device, related_name="vars")
    var_type = models.CharField("Type", max_length=10, choices=TYPE_CHOCES)
    units = models.CharField(max_length=10, blank=True)
    value = models.FloatField(default=0)
    description = models.CharField(max_length=255, blank=True)
    # TODO: Add magnitude
