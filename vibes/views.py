from django.shortcuts import render
from .models import Music

//Music Api
def index(request):
    songs=Music.objects.all()
    return render(request,"index.html",{})
