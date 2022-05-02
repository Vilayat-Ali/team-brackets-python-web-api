from django.db import models

from member.models import member as memberModel

# Choices
status_choices = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
    ('9th', '9th'),
    ('10th', '10th'),
    ('N/A', 'N/A'),
)

# achievement model
class achievement(models.Model):
    hackathon_name = models.CharField(max_length=35, blank=False, default="Hack'2x")
    status = models.CharField(max_length=5, choices=status_choices, default='N/A')
    team = models.ManyToManyField(memberModel)

    def __str__(self):
        return self.hackathon_name

