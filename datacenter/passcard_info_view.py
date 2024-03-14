from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from .duration_functions import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_id = passcard.id

    this_passcard_visits = list()
    visits = Visit.objects.filter(passcard_id=this_passcard_id)
    for visit in visits:
        this_passcard_visit = dict()
        this_passcard_visit['entered_at'] = visit.entered_at
        this_passcard_visit['duration'] = format_duration(get_duration(visit))
        this_passcard_visit['is_strange'] = is_visit_long(visit)
        this_passcard_visits.append(this_passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
