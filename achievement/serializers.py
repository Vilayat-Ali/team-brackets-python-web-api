from rest_framework import serializers

# importing model
from member.models import member as memberModel
from .models import achievement

class memberSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(many=True)
    skill = serializers.StringRelatedField(many=True)
    nationality = serializers.StringRelatedField(many=False)
    class Meta:
        model = memberModel
        fields = ['id', 'name', '']

class achievementSerializer(serializers.ModelSerializer):
    team = memberSerializer(many=True, read_only=True)
    class Meta:
        model = achievement
        fields = '__all__'