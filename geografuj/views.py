from django.shortcuts import render

def index(request):
    return render(request, "geografuj/index.html")


# Create your views here.
