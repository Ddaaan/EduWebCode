from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def main_index(request):
    return render(request, "mainpage.html")

def post(request):
    return render(request, 'post.html')