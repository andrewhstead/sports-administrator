from django.shortcuts import render, redirect, get_object_or_404
from data.models import Sport, Country, Competition, Season, Edition
from users.models import User
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import LoginForm, NewCompetitionForm, EditCompetitionForm, SiteSetupForm, SiteColorForm, NewEditionForm


# Create your views here.
def cms_home(request):
    
    user = request.user
    
    if user.is_authenticated:
        competitions = Competition.objects.all()
    
        return render(request, "cmshome.html", {'competitions': competitions})
        
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
        'form': form,
        'button_text': 'Create Competition'
    }
    
    args.update(csrf(request))
    return render(request, 'new_competition.html', args)
    

# Edit an existing competition.
@login_required(login_url='/login/')
def competition_details(request, competition_id):
    competition = get_object_or_404(Competition, pk=competition_id)
    editions = Edition.objects.filter(competition=competition.id).order_by('-season')

    if request.method == 'POST':
        form = EditCompetitionForm(request.POST, instance=competition)
        if form.is_valid():
            form.save()

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
    

# Edit an existing edition of a competition.
@login_required(login_url='/login/')
def edition_details(request, competition_id, edition_id):
    
    competition = Competition.objects.get(pk=competition_id)
    edition = Edition.objects.get(pk=edition_id)

    return render(request, 'edition_details.html', {'competition': competition, 'edition': edition})
    

# Add a new edition of a competition.
@login_required(login_url='/login/')    
def new_edition(request, competition_id):

    if request.method == 'POST':
        form = NewEditionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Edition has been created.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to create the new edition. Please try again.')

    else:
        form = NewEditionForm()

    args = {
        'form': form,
        'button_text': 'Create Competition'
    }
    
    args.update(csrf(request))
    return render(request, 'new_edition.html', args)