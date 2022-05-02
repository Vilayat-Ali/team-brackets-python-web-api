from django.urls import path

# importing views
from .views import *

urlpatterns = [
    path('all', getAllMembers, name="get_all_members"),
    path('<id_tag>', getMemberByID, name="get_member_by_id"),
]
