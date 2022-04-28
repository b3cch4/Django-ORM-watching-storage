from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import get_duration
from .models import format_duration


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    serialized_non_closed_visits = []
    for visit in non_closed_visits:
        if not visit.leaved_at:
            serialized_non_closed_visits.append(
                {
                    'who_entered': str(visit.passcard),
                    'entered_at': visit.entered_at,
                    'duration': format_duration(get_duration(visit))
                }
            )

    context = {
        'non_closed_visits': serialized_non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
