from django.shortcuts import render

# Create your views here.
def cms_home(request):

	return render(request, "cmshome.html")