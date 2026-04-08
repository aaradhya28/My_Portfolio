from django.shortcuts import render,get_object_or_404
from .models import Project
from .models import Certificate, Project

def home(request):
    certificates = Certificate.objects.all()
    projects = Project.objects.all()
    
    return render(request, 'home.html', {
        'certificates': certificates,
        'projects': projects
    })

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_detail.html', {'project': project})