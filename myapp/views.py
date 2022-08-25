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

    context= {
        'homes':homes,
        'abouts':abouts,
        'skills':skills,
        'education':education,
        'experiences':experiences,
        'services':services,
        'projects':projects,
        'allskills':allskills,


    }

    return render(request, 'index-3.html',context)
