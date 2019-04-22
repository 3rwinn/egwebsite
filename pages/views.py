from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project



def index(request):
    projects = Project.objects.order_by('-project_date').filter(is_published=True)[:6]
    context = {
        'projects': projects
    }
    return render(request, "pages/index.html", context)