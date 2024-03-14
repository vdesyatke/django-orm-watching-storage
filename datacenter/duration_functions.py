from django.utils.timezone import localtime, now
import datetime


def get_duration(visit):
    start = localtime(visit.entered_at)
    if visit.leaved_at:
        end = visit.leaved_at
    else:
        end = now()
    delta = end - start
    delta = delta - datetime.timedelta(microseconds=delta.microseconds)
    return delta


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int((seconds - 3600 * hours) // 60)
    return f'{hours}ч {minutes}мин'


def is_visit_long(visit, minutes=60):
    delta = get_duration(visit)
    return delta.total_seconds() > minutes * 60
