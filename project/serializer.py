from rest_framework import serializers

from .models import tech, project
from member.models import member as memberModel 

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberModel
        fields = ['id', 'name']

class projectSerializer(serializers.ModelSerializer):
    contributors = memberSerializer(many=True, read_only=True)
    hackathon = serializers.StringRelatedField(many=True)
    tech = serializers.StringRelatedField(many=True)
    class Meta:
        model = project 
        fields = '__all__'