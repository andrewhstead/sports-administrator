from django.shortcuts import render
from data.models import Sport, Country, Competition

# Create your views here.
def cms_home(request):
    
    competitions = Competition.objects.all()
    
    return render(request, "cmshome.html", {'competitions': competitions})