"""sportsadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cms import views as cms_views
from home import views as home_views

urlpatterns = [
    path(r'', home_views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('cms/', cms_views.cms_home, name='cms_home'),
    path('cms/clubs/new/', cms_views.new_club, name='new_club'),
    path('cms/clubs/<club_slug>/', cms_views.club_details, name='club_details'),
    path('cms/clubs/<club_slug>/seasons/<str:season>/', cms_views.club_season, name='club_season'),
    path('cms/competitions/<int:competition_id>/', cms_views.competition_details, name='competition_details'),
    path('cms/competitions/<int:competition_id>/editions/<int:edition_id>/', cms_views.edition_details, name='edition_details'),
    path('cms/competitions/<int:competition_id>/editions/new/', cms_views.new_edition, name='new_edition'),
    path('cms/competitions/new/', cms_views.new_competition, name='new_competition'),
    path('cms/configuration/', cms_views.configuration, name='configuration'),
    path('cms/login/', cms_views.login, name='login'),
    path('cms/players/new/', cms_views.new_player, name='new_player'),
    path('cms/players/<first_name>-<last_name>/<player_id>/', cms_views.player_details, name='player_details'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)