from django.urls import path

# importing views
from .views import *

urlpatterns = [
    path('all', getAllAchievements, name="get_all_achievements"),
]
