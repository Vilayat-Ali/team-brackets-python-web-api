from django.db import models
from django_countries.fields import CountryField

# role model
class memberRole(models.Model):
    role = models.CharField(max_length=50, blank=False, unique=True)
    def __str__(self):
        return self.role

# skill model
class memberSkill(models.Model):
    skill = models.CharField(max_length=50, blank=False, unique=True)
    def __str__(self):
        return self.skill

# member model
class member(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    role = models.ManyToManyField(memberRole)
    skill = models.ManyToManyField(memberSkill)
    nationality = CountryField()
    about = models.TextField(max_length=150, blank=False)
    github_url = models.CharField(max_length=125, blank=False, null=False, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name', 'github_url']


