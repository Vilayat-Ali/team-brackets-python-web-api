from rest_framework import serializers
from .models import *

class memberRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberRole
        fields = ['role']

class memberSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberSkill
        fields = ['skill']

class memberNationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = memberNationalitie
        fields = ['nationality']

class memberSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(many=True)
    skill = serializers.StringRelatedField(many=True)
    nationality = serializers.StringRelatedField(many=False)
    class Meta:
        model = member
        fields = '__all__'