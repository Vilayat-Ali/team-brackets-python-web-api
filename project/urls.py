from django.urls import path

from .views import *


urlpatterns = [
    path('all', getAllProject, name="get all projects"),
    path('<idTag>', getSpecificProject, name="get specific project"),
]
