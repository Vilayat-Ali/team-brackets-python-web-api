from rest_framework.response import Response
from rest_framework.decorators import api_view

# importing models
from .models import achievement
from member.models import member

# importing serializers
from .serializers import achievementSerializer

# get all achievements
@api_view(['GET'])
def getAllAchievements(request):
    try:
        achievements = achievement.objects.all()
        serialized_achievements = achievementSerializer(achievements, many=True).data
        return Response({ 'ok': True, 'message': 'fetched achievements successfully...', 'achievements': serialized_achievements})
    except Exception as e:
        return Response({ 'ok': False, 'message': str(e)})