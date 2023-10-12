from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'html_files/About_Me.html')

def my_portfolio(request):
    return render(request, 'html_files/my_portfolio.html')

def project_skills(request):
    return render(request, 'html_files/proj.html')

def contact(request):
    return render(request, 'html_files/contact.html')
