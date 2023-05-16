from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Find a Dino!</h1>")

def about(request):
    return HttpResponse("<h1>This is a dinosaur catalog website.</h1>")