from rest_framework import serializers

# importing model
from member.models import member as memberModel
from project.models import project as projectModel
from .models import achievement

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberModel
        fields = ['id', 'name']

class achievementSerializer(serializers.ModelSerializer):
    team = memberSerializer(many=True, read_only=True)
    class Meta:
        model = achievement
        fields = '__all__'