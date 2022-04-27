from django.db import models

from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    delta = localtime() - visit.entered_at
    total_seconds = delta.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    duration = f'{hours}:{minutes}'
    return duration


def format_duration(duration):
    splinted_my_str = duration.split(':')
    hours = splinted_my_str[0]
    minutes = splinted_my_str[-1]
    return f'{hours}ч {minutes}мин'


def is_visit_long(visit, minutes=60):
    delta = visit.leaved_at - visit.entered_at
    total_seconds = delta.total_seconds()
    dedicated_hours = int(total_seconds // 3600)
    dedicated_minutes = int((total_seconds % 3600) // 60)
    duration_in_minutes = (dedicated_hours * 60) + dedicated_minutes
    return duration_in_minutes > minutes
