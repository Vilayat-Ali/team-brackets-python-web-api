from rest_framework.response import Response
from rest_framework.decorators import api_view

# importing models
from .models import achievement

# importing serializers
from .serializers import achievementSerializer

# get all achievements
@api_view(['GET'])
def getAllAchievements(request):
    try:
        achievements = achievement.objects.all()
        print("Hackathon name: ", achievements[0].hackathon_name)
        print("Hackathon status: ", achievements[0].status)
        print("Hackathon team: ", achievements[0].team)
        serialized_achievements = achievementSerializer(achievements, many=True).data
        print(achievementSerializer(achievements).data)
        return Response({ 'ok': True, 'message': 'Achievements working', 'achievements': serialized_achievements})
    except Exception as e:
        return Response({ 'ok': False, 'message': str(e)})