from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('views/index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('views/about-us.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('views/contact-us.html')
    return HttpResponse(template.render())

def services(request):
    template = loader.get_template('views/our-services.html')
    return HttpResponse(template.render())
