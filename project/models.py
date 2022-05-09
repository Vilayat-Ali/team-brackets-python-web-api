from django.db import models

from member.models import member as memberModel
from achievement.models import achievement as achievementModel


class tech(models.Model):
    tech = models.CharField(max_length=25, blank=False, unique=True)

    def __str__(self):
        return self.tech

class project(models.Model):
    project_name = models.CharField(max_length=55, blank=False, unique=True)
    description = models.TextField(max_length=250, blank=False, unique=False)
    contributors = models.ManyToManyField(memberModel)
    hackathon = models.ForeignKey(achievementModel, on_delete=models.CASCADE)
    tech = models.ManyToManyField(tech)
    youtube_link = models.URLField(max_length=150, blank=False, unique=True)
    github_link = models.URLField(max_length=150, blank=False, unique=True)

    def __str__(self):
        return self.project_name
