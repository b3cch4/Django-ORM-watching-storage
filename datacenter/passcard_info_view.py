from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    visits_of_particular_guest = Visit.objects.filter(
        passcard=passcard
    )

    serialized_visits_of_particular_guest = []
    for visit in visits_of_particular_guest:
        if visit.leaved_at:
            serialized_visits_of_particular_guest.append(
                {
                    'entered_at': visit.entered_at,
                    'duration': visit.leaved_at - visit.entered_at,
                    'is_strange': is_visit_long(visit)
                }
            )

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits_of_particular_guest
    }
    return render(request, 'passcard_info.html', context)
