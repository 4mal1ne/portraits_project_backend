from django.shortcuts import render
from main_app.models import *


def home(request):
    data = Works.objects.all()
    return render(request, 'ui_templates/home.html', {"data": data})
