from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models


class Kid(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True, default='Unnamed')
    user = models.ForeignKey(User, blank=True, null=True)

    created  = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return '%s, kid of %s' % (self.name, self.user.username)

class Event(models.Model):

    TYPES = (
        ('f', 'Feeding'),
        ('fl', 'Feed Left'),
        ('fr', 'Feed Right'),
        ('d', 'Dirties'),
        ('e', 'Pee'),
        ('o', 'Poop'),
        ('p', 'Pumping'),
        ('pl', 'Pump Left'),
        ('pr', 'Pump Right'),
    )

    user = models.ForeignKey(User, blank=True, null=True)
    kid = models.ForeignKey(Kid, blank=True, null=True)
    typ   = models.CharField(choices=TYPES, max_length=2)

    created  = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return '%s at %s' % (self.get_typ_display(), self.created)


@receiver(post_save, sender=User)
def create_kid(sender, instance, created, **kwargs):
    """Create a matching kid whenever a user object is created."""
    if created: 
        kid, new = Kid.objects.get_or_create(user=instance)
