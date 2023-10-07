from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from . serializers import ProjectSerializer
from projects.models import Project, Review, Tag


# views that gonna tells us how many routes are in it 
@api_view(['GET'])
def getRoutes(request):
    routes = [
        # method it gonna takes and the url
        {'GET' : '/api/projects'},
        {'GET' : '/api/projects/id'},
        {'POST' : '/api/projects/id/vote'},

        # builtin routes
        {'POST' : '/api/users/token'},
        # when the user token get expires they can refresh it increase it's time to live 
        {'POST' : '/api/users/token/refresh'}
    ]
    # safe tells that we can send other data structure also instead of the dictionary 
    # return Response(routes, safe=False) because using the DRF or decorators we don't need this 
    return Response(routes)

# user needs to be authenticated 
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    print("USER", request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProject(request,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,
    )
    # created in the above is true or false, in review either the objects get store or the objects get created
    review.value = data['value']
    review.save()
    project.getVoteCount
    # call this, model funnction in reviews, bcz we after voting we want to update the vote count 
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)
    
    return Response('Tag was deleted!')