from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import get_duration
from .models import format_duration


def storage_information_view(request):
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in not_leaved_visits:
        if not visit.leaved_at:
            non_closed_visits.append(
                dict(
                    who_entered=str(visit.passcard),
                    entered_at=visit.entered_at,
                    duration=format_duration(get_duration(visit))
                )
            )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
