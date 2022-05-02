from rest_framework import serializers

# importing model
from member.models import member as memberModel
from .models import achievement

class achievementMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberModel
        fields = ['id', 'name']

class achievementSerializer(serializers.ModelSerializer):
    team = achievementMemberSerializer(many=True, read_only=True)
    class Meta:
        model = achievement
        fields = '__all__'