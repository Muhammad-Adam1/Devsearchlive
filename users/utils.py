from django.db.models import Q 
from .models import Profile, Skill


def SearchProjects(request):
    # getting the search query of the profile from the front 
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    # getting the searched skills from the database
    skills = Skill.objects.filter(name__icontains=search_query)

    # getting the distinct profiles from database on bases of these attributes 
    profiles = Profile.objects.distinct().filter( Q(name__icontains=search_query) | 
                                        Q(short_intro__icontains=search_query) |
                                        Q(skill__in=skills))
    return profiles, search_query