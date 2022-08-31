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
    address=Address.objects.all()
    mycvs=MyCV.objects.all()
    achievments=Achiev.objects.all()

    context= {
        'homes':homes,
        'abouts':abouts,
        'skills':skills,
        'education':education,
        'experiences':experiences,
        'services':services,
        'projects':projects,
        'allskills':allskills,
        'testimonials':testimonials,
        'address':address,
        'mycvs':mycvs,
        'achievments':achievments
    }

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        comments=request.POST['comments']

        return render(request,'index-3.html',{'name':name})
    else:
        return render(request, 'index-3.html',context)

def allprojects(request):
    projects=Projects.objects.all()
    address=Address.objects.all()
    abouts=About.objects.all()


    context={
        'projects':projects,
        'address':address,
        'abouts':abouts,

    }

    return render (request, 'projects.html',context)

def project(request,project_id):
    singleproject=Projects.objects.get(id=project_id)
    address=Address.objects.all()
    abouts=About.objects.all()

    context={
        'singleproject':singleproject,
        'address':address,
        'abouts':abouts,


    }

    return render (request, 'singleproject.html',context)

