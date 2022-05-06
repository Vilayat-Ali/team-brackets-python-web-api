from django.contrib import admin

from .models import project, tech

admin.site.register(tech)
admin.site.register(project)
