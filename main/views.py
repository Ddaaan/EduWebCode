from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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

def stuSur_question(request):
    questions = [
        {'id' : 1, 'text' : '1번 문제 테스트입니다.'},
        {'id' : 2, 'text' : '2번 문제 테스트입니다.'}
    ]
    options = range(1, 6)
    return render(request, 'student_survey.html', {'questions' : questions, 'options' : options})

# 로그인 화면 
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})