from django.db.models import Q 
from .models import Profile, Skill

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProfiles(request, profiles, results):
    # get 1st set of three pages
    page = request.GET.get('page')   #returns a number that which page number is requested 
    # results = 3 how projects should be display on the project
    paginator = Paginator(profiles, results)

    try:
        # retrives requested set of page from the results (paginator)
        profiles = paginator.page(page)
    except PageNotAnInteger:
        # when loads the page first time we get the error bcz we didn't request any page
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        # this tells how many pages we have and we redirect the user to the last page 
        page = paginator.num_pages
        profiles = paginator.page(page)

    # leftIndex is used for the number of paginations on left side of the selected number, page - 1  means show one 
    # pagination on the left side 
    leftIndex = (int(page) - 4)
    # if the substraction result is less than one than set it's value '1'
    if leftIndex < 1:
        leftIndex = 1

    # rightIndex is used for the number of paginations on right side of the selected number, page + 1  means show one 
    # pagination on the rigth side
    rightIndex = (int(page) + 5)
    # if the addition result is more than the total pages i.e., paginator.num_pages, set it's value to that no. of pages
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    # creating custom range to create the rolling window   |1, 2, 3, """4""" , 5, 6, 7|
    custom_range = range(leftIndex,rightIndex)
    return custom_range, profiles

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