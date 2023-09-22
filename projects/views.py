from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    context = {'project':projectObject}
    return render(request, 'projects/single-project.html', context)

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project-form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    context = {}
    templates = 'projects/project-form.html'
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # here we tell that which object we are going to modify 
        if form.is_valid:
            form.save()
            return redirect('projects')

    context['form'] = form
    return render(request, templates, context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete.html', {"object":project})