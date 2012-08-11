from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
from events.models import Kid, Event
import datetime


def home(request):
    if request.user.is_authenticated():
        return home_user(request)
    else:
        return home_public(request)

@login_required
@render_to('home-user.html')
def home_user(request):

    kids = Kid.objects.filter(user=request.user)
    if 'child' in request.GET:
        kid = get_object_or_404(Kid, id=request.GET.get('child'), user=request.user)
    else:
        kid = kids[0]

    events = Event.objects.filter(user=request.user, kid=kid).order_by('-created')

    feedings = events.filter(typ__in=['f', 'fl', 'fr'], created__gte=datetime.datetime.now() - datetime.timedelta(hours=24))
    pumpings = events.filter(typ__in=['p', 'pl', 'pr'], created__gte=datetime.datetime.now() - datetime.timedelta(hours=24))
    dirties  = events.filter(typ__in=['d', 'e', 'o'], created__gte=datetime.datetime.now() - datetime.timedelta(hours=24))
    pees     = events.filter(typ='e', created__gte=datetime.datetime.now() - datetime.timedelta(hours=24))
    poops    = events.filter(typ='o', created__gte=datetime.datetime.now() - datetime.timedelta(hours=24))

    feedings_last_24hrs = feedings.count()
    pumpings_last_24hrs = pumpings.count()
    pees_last_24hrs     = pees.count()
    poops_last_24hrs    = poops.count()

    if feedings.count():
        last_feeding = feedings[0].created
    else:
        last_feeding = False
    if pumpings.count():
        last_pumping = pumpings[0].created
    else:
        last_pumping = False
    if dirties.count():
        last_dirty   = dirties[0].created
    else:
        last_dirty = False

    return {
        'kid': kid,
        'kids': kids,
        'events': events[:100],
        'last_feeding': last_feeding,
        'last_pumping': last_pumping,
        'last_dirty': last_dirty,
        'feedings_last_24hrs': feedings_last_24hrs,
        'pees_last_24hrs': pees_last_24hrs,
        'poops_last_24hrs': poops_last_24hrs,
        'pumpings_last_24hrs': pumpings_last_24hrs,
    }

@render_to('home-public.html')
def home_public(request):

    return {}
