from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from events.models import Kid, Event


def add(request, type):

    kid = get_object_or_404(Kid, id=request.GET.get('child'))

    event = Event(
        user=request.user,
        kid=kid,
        typ=type,
    )
    event.save()

    return HttpResponseRedirect('/?n&child=%d' % kid.id)

def delete(request, id):

    kid = get_object_or_404(Kid, id=request.GET.get('child'))

    event = get_object_or_404(Event, user=request.user, pk=id)
    event.delete()
    return HttpResponseRedirect('/?child=%d' % kid.id)
