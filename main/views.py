from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Project, Portfolio,PageView,Ml_Projects
from .forms import PortfolioForm

@login_required
def dashboard(request):
    projects = Portfolio.objects.all()
    return render(request, 'portfolio/dashboard.html', {'projects': projects})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/add_project.html', {'form': form})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Portfolio, pk=pk)
    form = PortfolioForm(request.POST or None, request.FILES or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'portfolio/edit_project.html', {'form': form})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Portfolio, pk=pk)
    project.delete()
    return redirect('dashboard')

def home(request):
    projects = Project.objects.all()
    portfolio = Portfolio.objects.first()  # Assuming you want the first portfolio entry
    mlprojecs = Ml_Projects.objects.all()
    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'portfolio': portfolio,
        'mlprojecs':mlprojecs,
    }
    )

def skills_page(request):
    page, created = PageView.objects.get_or_create(page_name='skills')
    page.count += 1
    page.save()

    return render(request, 'skills.html', {'views': page.count})

# main/views.py

def project_page(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_page(request):
    mlprojecs = Ml_Projects.objects.all()
    return render(request, 'projects.html', {'mlprojecs': mlprojecs})

def about_page(request):
    page, created = PageView.objects.get_or_create(page_name='about')
    page.count += 1
    page.save()
    
    return render(request, 'about.html', {'views': page.count})
