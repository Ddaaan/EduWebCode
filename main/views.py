from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def main_index(request):
    return render(request, "mainpage.html")

def post(request):
    return render(request, 'post.html')

def about1(request):
    return render(request, 'about1.html')

def about2(request):
    return render(request, 'about2.html')

def file(request):
    return render(request, 'file.html')

def admin(request):
    return render(request, 'admin.html')

def student_survey(request):
    return render(request, 'student_survey.html')