from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . models import Project
from .forms import ProjectForm

from .utils import SearchProjects

def projects(request):
    # searching the query using the utils file, so not to create mess 
    projects, search_query = SearchProjects(request)

    # passing search_query so that the input have the search value 
    context = {'projects': projects, 'search_query':search_query}

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    context = {'project':projectObject}
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def createProject(request):
    profile  = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'projects/project-form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    templates = 'projects/project-form.html'
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # here we tell that which object we are going to modify 
        if form.is_valid:
            form.save()
            return redirect('account')

    context = {'form':form}
    return render(request, templates, context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {"object":project}
    return render(request, 'delete.html', context)