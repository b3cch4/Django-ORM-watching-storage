from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import is_visit_long



def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    visits_by_specific_owner = Visit.objects.filter(
        passcard=passcard
    )

    this_passcard_visits = []
    for visit in visits_by_specific_owner:
        if visit.leaved_at:
            this_passcard_visits.append(
                {
                    'entered_at': visit.entered_at,
                    'duration': visit.leaved_at - visit.entered_at,
                    'is_strange': is_visit_long(visit)
                }
            )


    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
