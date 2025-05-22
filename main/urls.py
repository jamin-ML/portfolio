from django.urls import path
from . import views

urlpatterns = [
    path('Project/', views.Project, name='project'),
    path('Portfolio/', views.Portfolio, name='Portfolio'),
    path('skills/', views.skills_page, name='skills'),
    path('projects/', views.project_page, name='projects'),
    path('about/',views.about_page,name='about'),
    path('ml',views.Ml_Projects,name='ml'),
    
]