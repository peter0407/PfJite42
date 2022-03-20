import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "hello/index.html")
#HttpResponse("this is index")


def peter(request):
    return HttpResponse("my name is peter")


def greet(request):
    now = datetime.datetime.now()
    return render(request, "hello/greet.html", {
        "birthday": now.month == 8 and now.day == 2
    })
