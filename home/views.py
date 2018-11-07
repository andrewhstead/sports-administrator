from django.shortcuts import render
from users.models import User
from football.models import Edition, Club, LeagueRecord

# Create your views here.
def home_page(request):
    
    user = User.objects.get(pk=1)
    site_name = user.site_name
    
    edition = Edition.objects.get(pk=34)
    clubs = LeagueRecord.objects.filter(edition=edition).order_by('-total_points', '-table_tiebreaker', '-total_for', 'full_name')
    
    primary_color = user.primary_color
    secondary_color = user.secondary_color
    primary_text = user.primary_text
    secondary_text = user.secondary_text
    
    return render(request, "home.html", {
        'site_name': site_name, 
        'primary_color': primary_color, 
        'secondary_color': secondary_color, 
        'primary_text': primary_text, 
        'secondary_text': secondary_text,
        'clubs': clubs
    })