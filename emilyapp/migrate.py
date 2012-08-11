from django.contrib.auth.models import User
from events.models import Event, Kid

def go():
    us = User.objects.all()

    for u in us:
        kid = Kid(
            name='Unnamed',
            user=u
        )
        kid.save()

    for e in Event.objects.all():
        e.kid = Kid.objects.get(user=e.user)
        e.save()
