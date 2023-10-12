from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("my_portfolio/", views.my_portfolio, name="my_portfolio"),
    path("project_skills/", views.project_skills, name="project_skills"),
    path("contact/", views.contact, name="contact"),
    
]