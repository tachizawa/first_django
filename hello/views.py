import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello Under World")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )