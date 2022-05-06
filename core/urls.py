from django.contrib import admin
from django.urls import path, include

# admin dashboard customization
admin.site.site_header = "Team Brackets Admin"
admin.site.site_title = "Team Brackets"
admin.site.index_title = "Admin Dashboard"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/member/', include('member.urls')),
    path('api/achievement/', include('achievement.urls')),
    path('api/project/', include('project.urls')),
]
