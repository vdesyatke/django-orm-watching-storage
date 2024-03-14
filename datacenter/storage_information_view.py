from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .duration_functions import get_duration, format_duration


def storage_information_view(request):
    passcards = Passcard.objects.all()
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = list()
    for visit in active_visits:
        visitor = passcards.filter(id=visit.passcard_id)[0]
        non_closed_visit = {
            'who_entered': visitor.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
        }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
