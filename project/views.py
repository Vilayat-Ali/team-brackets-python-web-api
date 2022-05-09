from rest_framework.response import Response
from rest_framework.decorators import api_view

# models
from .models import project as projectModel

# serializers
from .serializer import projectSerializer


@api_view(['GET'])
def getAllProject(request):
    try:
        projects = projectModel.objects.all() 
        serialized_projects = projectSerializer(projects, many=True)
        return Response({
            'ok': True,
            'message': 'Projects retrieved successfully...',
            'products': serialized_projects.data
        })
    except Exception as e:
        return Response({ 'ok': False, 'message': e })

@api_view(['GET'])
def getSpecificProject(request, idTag):
    try:
        project = projectModel.objects.get(id = idTag)
        serialized_project = projectSerializer(project, many=False)
        return Response({
            'ok': True,
            'message': 'Projects retrieved successfully...',
            'product': serialized_project.data
        })
    except Exception as e:
        return Response({ 'ok': False, 'message': str(e)})

@api_view(['GET'])
def getProjectByHack(request, hack):
    try:
        project = projectModel.objects.get(hackathon__hackathon_name=hack)
        serialized_project = projectSerializer(project, many=False)
        return Response({
            'ok': True,
            'message': 'Projects retrieved successfully...',
            'product': serialized_project.data
        })
    except Exception as e:
        return Response({'ok': False, 'message': str(e)})

@api_view(['GET'])
def getProjectByProjectName(request, projectName):
    try:
        project = projectModel.objects.get(project_name=projectName)
        serialized_project = projectSerializer(project, many=False)
        return Response({
            'ok': True,
            'message': 'Projects retrieved successfully...',
            'product': serialized_project.data
        })
    except Exception as e:
        return Response({'ok': False, 'message': str(e)})
