from django.shortcuts import render
from .models import *
# Create your views here.

def welcome(request):
    homes=Home.objects.all()
    abouts=About.objects.all()
    skills=Skills.objects.all()
    education=Education.objects.all()
    experiences=Experience.objects.all()
    services=Services.objects.all()
    projects=Projects.objects.all()
    allskills=AllSkills.objects.all()
    testimonials=Testimonials.objects.all()

    context= {
        'homes':homes,
        'abouts':abouts,
        'skills':skills,
        'education':education,
        'experiences':experiences,
        'services':services,
        'projects':projects,
        'allskills':allskills,
        'testimonials':testimonials


    }

    return render(request, 'index-3.html',context)

def allprojects(request):
    projects=Projects.objects.all()

    context={
        'projects':projects
    }

    return render (request, 'projects.html',context)

def project(request,project_id):
    singleproject=Projects.objects.get(id=project_id)

    context={
        'singleproject':singleproject
    }

    return render (request, 'singleproject.html',context)

