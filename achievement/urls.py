from django.urls import path

# importing views
from .views import *

urlpatterns = [
    path('<int:page>/<int:limit>', getAchievements, name="get_all_achievements"),
]
