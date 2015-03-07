from django.db import models
from vars.models import Var
from windows.models import Window


class Mimic(models.Model):
    """A human friendly group of vars in a :class:`~windows.models.Window`."""
    name = models.CharField(max_length=50, blank=True)
    vars = models.ManyToManyField(Var, null=True, blank=True)
    window = models.ForeignKey(Window, related_name='mimics')
    x = models.SmallIntegerField(null=True, blank=True, default=0)
    y = models.SmallIntegerField(null=True, blank=True, default=0)
    # TODO: Add image field

    def __unicode__(self):
        return self.name