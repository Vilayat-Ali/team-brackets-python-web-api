from django.urls import path

from .views import *


urlpatterns = [
    path('all', getAllProject, name="get all projects"),
    path('id/<int:idTag>', getSpecificProject, name="get specific project by id"),
    path('hack/<hack>', getProjectByHack, name="get specific project by hackathon"),
    path('name/<projectName>', getProjectByProjectName, name="get specific project by hackathon project name"),
]
