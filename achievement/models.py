from django.db import models

from member.models import member as memberModel

# Choices
status_choices = (
    ('Not Decided', 'Not Decided'),
    ('Winner', 'Winner'),
    ('Runner Up', 'Runner Up'),
    ('Track Winner', 'Track Winner'),
)

# achievement model
class achievement(models.Model):
    hackathon_name = models.CharField(max_length=35, blank=False, default="Hack'2x")
    status = models.CharField(max_length=12, choices=status_choices, default='Not Decided')
    team = models.ManyToManyField(memberModel)

    def __str__(self):
        return self.hackathon_name

