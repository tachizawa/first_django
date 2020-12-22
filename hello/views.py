import re
from datetime import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Under World")

def home_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y as %X")

    match_object = re.match("[a-zA-Z]+")