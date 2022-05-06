from django.contrib import admin
from django.urls import path, include

# admin dashboard customization
admin.site.site_header = "Team Brackets Admin"
admin.site.index_title = "Admin Dashboard"
admin.site.site_title = "Team Brackets"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/member/', include('member.urls')),
    path('api/achievement/', include('achievement.urls')),
]
