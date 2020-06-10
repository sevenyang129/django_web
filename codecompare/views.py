
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,"register.html")


def task(request):
    return render(request,'index.html')

def add_task(request):
    return render(request,'add_task.html')

def edit_task(request):
    return render(request,'edit_task.html')

def code_diff(request):
    return render(request,'code_diff.html')