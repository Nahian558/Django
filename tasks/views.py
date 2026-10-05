from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse("<p style='color:green; font-size:150px'>hello my world!</p>")

def show_task(response):
    return HttpResponse("This is show task page!")