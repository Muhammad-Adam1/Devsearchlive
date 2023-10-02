from django.db.models import Q

from . models import Project, Tag

def SearchProjects(request):
    # getting the search query of the profile from the front 
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # searching the projects on the base of the tags
    tags = Tag.objects.filter(name__icontains=search_query)

    # getting the distinct projects from database on bases of these attributes
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query