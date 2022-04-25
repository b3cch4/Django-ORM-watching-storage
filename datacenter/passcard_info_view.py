from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import is_visit_long



def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    visits_by_specific_owner = Visit.objects.filter(
        passcard=Passcard.objects.get(passcode=passcode)
    )

    this_passcard_visits = []
    for visit in visits_by_specific_owner:
        if visit.leaved_at is not None:
            this_passcard_visits.append(
                dict(
                    entered_at=visit.entered_at,
                    duration=visit.leaved_at - visit.entered_at,
                    is_strange=is_visit_long(visit)
                )
            )


    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
