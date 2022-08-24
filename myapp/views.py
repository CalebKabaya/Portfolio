from django.shortcuts import render
from .models import *
# Create your views here.

def welcome(request):
    homes=Home.objects.all()
    abouts=About.objects.all()
    skills=Skills.objects.all()
    education=Education.objects.all()
    experiences=Experience.objects.all()

    context= {
        'homes':homes,
        'abouts':abouts,
        'skills':skills,
        'education':education,
        'experiences':experiences

    }

    return render(request, 'index-3.html',context)
