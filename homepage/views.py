from django.shortcuts import render

def index(request):
    return render(request, "../global_templates/index.html")


# Create your views here.
