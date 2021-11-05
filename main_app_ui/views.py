from django.shortcuts import render

from main_app.models import *


def home_page(request):
    data = Works.objects.all()
    return render(request, 'ui_templates/home_page.html', {'data': data})


def about_artist(request):
    pass


def portfolio(request):
    pass


def price(request):
    pass


def testimonials(request):
    pass
