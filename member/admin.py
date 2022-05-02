from django.contrib import admin

# importing models
from .models import *

# registering models
admin.site.register(memberNationalitie)
admin.site.register(memberRole)
admin.site.register(memberSkill)
admin.site.register(member)