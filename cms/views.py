from django.shortcuts import render, redirect, get_object_or_404
from data.models import Sport, Country, Competition
from users.models import User
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import LoginForm, NewCompetitionForm, EditCompetitionForm, ConfigurationForm


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
        'competition': competition
    }
    args.update(csrf(request))
    return render(request, 'competition_details.html', args)
    

@login_required(login_url='/login/')    
def configuration(request):
    user = request.user

    if request.method == 'POST':
        form = ConfigurationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been saved.')
            return redirect(reverse('cms_home'))
        else:
            messages.error(request, 'Sorry, we were unable to save your settings. Please try again.')

    else:
        form = ConfigurationForm(instance=user)

    args = {
        'form': form,
        'button_text': 'Confirm Settings'
    }
    
    args.update(csrf(request))
    return render(request, 'configuration.html', args)