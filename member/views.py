from rest_framework.response import Response
from rest_framework.decorators import api_view

# importing models
from .models import member

# importing serializers
from .serializers import memberSerializer

# fetch all members
@api_view(['GET'])
def getAllMembers(request):
    try:
        member_data = member.objects.all()
        serialized_member_data = memberSerializer(member_data, many=True)
        return Response({ 'ok': True, 'message': 'Retrieved member data successfully', 'members': serialized_member_data.data})
    except Exception as e:
        return Response({ 'ok': False, 'message': e })


# fetch specific member by id
@api_view(['GET'])
def getMemberByID(request, id_tag):
    try:
        member_data = member.objects.filter(id=id_tag)
        serialized_member_data = memberSerializer(member_data, many=True)
        return Response({ 'ok': True, 'message': 'Retrieved member data successfully', 'members': serialized_member_data.data})
    except Exception as e:
        return Response({ 'ok': False, 'message': e })

# fetch members by role
@api_view(['GET'])
def getMemberByRole(request, role_tag):
    try:
        member_data = member.objects.filter(role=role_tag)
        serialized_member_data = memberSerializer(member_data, many=True)
        return Response({ 'ok': True, 'message': 'Retrieved member data successfully', 'members': serialized_member_data.data})
    except Exception as e:
        return Response({ 'ok': False, 'message': e })

