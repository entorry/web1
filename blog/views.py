from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello Python.")

def hello(request):
    return HttpResponse('helloworlf')

def post(request):
    return HttpResponse('post...')

def comment(request):
    return HttpResponse("Comment")