from django.shortcuts import render
from users.models import User

# Create your views here.
def home_page(request):
    
    user = User.objects.get(pk=1)
    site_name = user.site_name
    
    return render(request, "home.html", {'site_name': site_name})