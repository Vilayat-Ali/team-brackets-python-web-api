from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/member/', include('member.urls')),
    path('api/achievement/', include('achievement.urls')),
]
