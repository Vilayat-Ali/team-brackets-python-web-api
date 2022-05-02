from django.contrib import admin

# importing models
from .models import achievement as achievementModel

# Register your models here.
admin.site.register(achievementModel)