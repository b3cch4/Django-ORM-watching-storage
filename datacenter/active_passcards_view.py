from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь

    context = {
        'active_passcards': Passcard.objects.filter(is_active=True),  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)