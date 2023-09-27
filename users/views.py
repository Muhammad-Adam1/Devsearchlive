from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import CustomeUserCreationForm, ProfileForm, SkillForm


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect("profiles")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,"Username or Password is incorrect")
    return render(request, "users/login_register.html")

def logoutUser(request):
    logout(request)
    messages.info(request,"User is logged out!")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomeUserCreationForm()

    if request.method == "POST":
        form = CustomeUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was created succesfully!")
            

            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, "An error has occured during registration")
    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects':projects}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account') 
    context = {'form':form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill was added succesfully!")
            return redirect('account')
    context = {'form':form}
    return render(request, "users/skill_form.html", context)

@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "skill was updated succesfully!")
            return redirect('account')
    context = {'form':form}
    return render(request, "users/skill_form.html", context)

@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    context = {'object':skill}

    if request.method == 'POST':
        skill.delete()
        messages.success(request, "skill was deleted succesfully!")
        return redirect('account')
    
    return render(request, 'delete.html', context)