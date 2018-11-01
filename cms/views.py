from django.shortcuts import render, redirect, get_object_or_404
from data.models import Sport, Country, Season
from football.models import Competition, Edition, Club, ClubSeason, LeagueRecord, Player
from users.models import User
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.template.defaultfilters import slugify
from .forms import LoginForm, NewCompetitionForm, EditCompetitionForm, SiteSetupForm, SiteColorForm, NewEditionForm, EditEditionForm, ClubForm, ClubSeasonForm, TableDetailsForm, HomeForm, AwayForm, PlayerForm


# Create your views here.
def cms_home(request):
    
    user = request.user
    
    if user.is_authenticated:
        competitions = Competition.objects.all().order_by('-date_modified')[:5]
        clubs = Club.objects.all().order_by('-date_modified')[:5]
        players = Player.objects.all().order_by('-date_modified')[:5]
        
        return render(request, "cmshome.html", {'competitions': competitions, 'clubs': clubs, 'players': players})
        
    else:
        
        return redirect(reverse('login'))


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect(request.GET.get('next') or reverse('cms_home'))
            else:
                messages.error(request, "Your username or password was not recognised. Please try again.")

    else:
        form = LoginForm()

    args = {'form': form}

    args.update(csrf(request))
    return render(request, 'login.html', args)
    

# Add a new competition.
@login_required(login_url='/login/')    
def new_competition(request):
    
    user = request.user

    if request.method == 'POST':
        form = NewCompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Competition has been created.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to create the competition. Please try again.')

    else:
        form = NewCompetitionForm()

    args = {
        'user': user,
        'form': form,
        'button_text': 'Create Competition'
    }
    
    args.update(csrf(request))
    return render(request, 'new_competition.html', args)
    

# Edit an existing competition.
@login_required(login_url='/login/')
def competition_details(request, competition_id):
    competition = get_object_or_404(Competition, pk=competition_id)
    editions = Edition.objects.filter(competition=competition.id).order_by('season')

    if request.method == 'POST':
        form = EditCompetitionForm(request.POST, instance=competition)
        if form.is_valid():
            update = form.save(False)
            competition.date_modified = timezone.now()
            update.save()

        messages.success(request, "Competition details successfully edited.")

        return redirect(reverse('cms_home'))

    else:
        form = EditCompetitionForm(instance=competition)

    args = {
        'form': form,
        'form_action': reverse('competition_details', kwargs={'competition_id': competition_id}),
        'button_text': 'Edit Details',
        'competition': competition,
        'editions': editions
    }
    args.update(csrf(request))
    return render(request, 'competition_details.html', args)
    

@login_required(login_url='/login/')    
def configuration(request):
    user = request.user

    if request.method == 'POST':
        setup_form = SiteSetupForm(request.POST, request.FILES, instance=user)
        color_form = SiteColorForm(request.POST, request.FILES, instance=user)
        if setup_form.is_valid() and color_form.is_valid():
            setup_form.save()
            color_form.save()
            messages.success(request, 'Your settings have been saved.')
            return redirect(reverse('configuration'))
        else:
            messages.error(request, 'Sorry, we were unable to save your settings. Please try again.')

    else:
        setup_form = SiteSetupForm(instance=user)
        color_form = SiteColorForm(instance=user)

    args = {
        'setup_form': setup_form,
        'color_form': color_form,
        'button_text': 'Update Settings'
    }
    
    args.update(csrf(request))
    return render(request, 'configuration.html', args)
    

# Add a new edition of a competition.
@login_required(login_url='/login/')    
def new_edition(request, competition_id):
    
    competition = Competition.objects.get(pk=competition_id)
    current = Edition.objects.get(competition_id=competition_id, is_current=True)

    if request.method == 'POST':
        form = NewEditionForm(request.POST, request.FILES)
        if form.is_valid():
            
            new_edition = form.save()
            if new_edition.is_current == True:
                current.is_current = False
                current.save()
            
            edition_teams = new_edition.teams.all()
            
            for team in edition_teams:
                
                # If the team already has a record for this season, use it to create their league record.
                try:
                    club_season = ClubSeason.objects.get(club=team, season=new_edition.season)
                    
                    if competition.format == 'league':
                        club_record = LeagueRecord(clubseason=club_season, edition=new_edition, full_name=team.full_name)
                        club_record.save()
                        
                # If the team has no record for this season, create one and then use it to create their league record.
                except ClubSeason.DoesNotExist:
                    club_season = ClubSeason(club=team, season=new_edition.season, full_name=team.full_name, short_name=team.short_name, abbreviation=team.abbreviation)
                    club_season.save()
                    
                    if competition.format == 'league':
                        club_record = LeagueRecord(clubseason=club_season, edition=new_edition, full_name=team.full_name)
                        club_record.save()
                    
            messages.success(request, 'Edition has been created.')
            return redirect(reverse('competition_details', args={competition.pk}))
        else:
            messages.error(request, 'Sorry, we were unable to create the new edition. Please try again.')

    else:
        form = NewEditionForm()

    args = {
        'competition': competition,
        'form': form,
        'button_text': 'Create Edition'
    }
    
    args.update(csrf(request))
    return render(request, 'new_edition.html', args)
    

# Edit an existing edition of a competition.
@login_required(login_url='/login/')
def edition_details(request, competition_id, edition_id):
    
    competition = Competition.objects.get(pk=competition_id)
    edition = Edition.objects.get(pk=edition_id)
    current = Edition.objects.get(competition_id=competition_id, is_current=True)
    clubs = LeagueRecord.objects.filter(edition=edition).order_by('full_name')
    
    if request.method == 'POST':
        form = EditEditionForm(request.POST, request.FILES, instance=edition)
        if form.is_valid():
            this_edition = form.save(False)
            
            if this_edition.is_current == True:
                current.is_current = False
                current.save()
            
            this_edition.save()

            messages.success(request, 'Edition has been edited.')
            return redirect(reverse('competition_details', args={competition.pk}))
        else:
            messages.error(request, 'Sorry, we were unable to edit the edition. Please try again.')

    else:
        form = EditEditionForm(instance=edition)

    args = {
        'competition': competition,
        'edition': edition,
        'clubs': clubs,
        'form': form,
        'button_text': 'Edit Details'
    }
    
    args.update(csrf(request))
    return render(request, 'edition_details.html', args)

# Add a new club.
@login_required(login_url='/login/')    
def new_club(request):

    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save(False)
            club.date_modified = timezone.now()
            club.slug = slugify(club.full_name)
            club.save()
            messages.success(request, 'Club has been created.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to create the club. Please try again.')

    else:
        form = ClubForm()

    args = {
        'form': form,
        'button_text': 'Create Club'
    }
    
    args.update(csrf(request))
    return render(request, 'new_club.html', args)
    

# Edit an existing club.
@login_required(login_url='/login/')
def club_details(request, club_slug):
    club = get_object_or_404(Club, slug=club_slug)
    seasons = LeagueRecord.objects.filter(club_id=club.id)

    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            update = form.save(False)
            club.date_modified = timezone.now()
            update.save()
            messages.success(request, 'Club has been edited successfully.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to edit the club. Please try again.')

    else:
        form = ClubForm(instance=club)

    args = {
        'form': form,
        'club': club,
        'seasons': seasons,
        'button_text': 'Edit Details'
    }
    
    args.update(csrf(request))
    return render(request, 'club_details.html', args)
    

# Edit a club season.
@login_required(login_url='/login/')
def club_season(request, club_slug, season):
    club = get_object_or_404(Club, slug=club_slug)
    season = get_object_or_404(Season, name=season)
    league_record = LeagueRecord.objects.get(club_id=club.id, season_id=season.id)

    if request.method == 'POST':
        season_form = ClubSeasonForm(request.POST, request.FILES, instance=league_record)
        table_form = TableDetailsForm(request.POST, request.FILES, instance=league_record)
        home_form = HomeForm(request.POST, request.FILES, instance=league_record)
        away_form = AwayForm(request.POST, request.FILES, instance=league_record)
        if season_form.is_valid() and table_form.is_valid() and home_form.is_valid() and away_form.is_valid():
            season_form.save()
            table_form.save()
            home_form.save()
            away_form.save()
            messages.success(request, 'Details have been edited successfully.')
            return redirect(reverse('club_details', args={club_slug}))
        else:
            messages.error(request, 'Sorry, we were unable to edit the details. Please try again.')

    else:
        season_form = ClubSeasonForm(instance=league_record)
        table_form = TableDetailsForm(instance=league_record)
        home_form = HomeForm(instance=league_record)
        away_form = AwayForm(instance=league_record)
        
    args = {
        'club': club,
        'season': season,
        'league_record': league_record,
        'season_form': season_form,
        'table_form': table_form,
        'home_form': home_form,
        'away_form': away_form,
        'button_text': 'Edit Details'
    }
    
    return render(request, 'club_season.html', args)
    

# Add a new player.
@login_required(login_url='/login/')    
def new_player(request):
    
    user = request.user

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player has been created.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to create the player. Please try again.')

    else:
        form = PlayerForm()

    args = {
        'user': user,
        'form': form,
        'button_text': 'Create Player'
    }
    
    args.update(csrf(request))
    return render(request, 'new_player.html', args)
    

# Edit an existing player.
@login_required(login_url='/login/')    
def player_details(request, first_name, last_name, player_id):
    player = get_object_or_404(Player, pk=player_id)

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            update = form.save(False)
            player.date_modified = timezone.now()
            update.save()
            messages.success(request, 'Player has been edited.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to edit the player. Please try again.')

    else:
        form = PlayerForm(instance=player)

    args = {
        'player': player,
        'form': form,
        'button_text': 'Edit Details'
    }
    
    args.update(csrf(request))
    return render(request, 'player_details.html', args)