from django import forms
from django.forms.widgets import TextInput
from users.models import User
from football.models import Competition, Edition, Club, Player
from django.core.exceptions import ValidationError


# Simple username and password login.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

# Form to create a new competition.
class NewCompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ['name', 'sport', 'country', 'type', 'format']
        labels = {
            'name': 'Competition Name',
            'sport': 'Sport',
            'country': 'Primary Country',
        }
    

# Form to edit a competition.
class EditCompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ['name', 'sport', 'country', 'type', 'format', 'is_active']
        labels = {
            'name': 'Competition Name',
            'sport': 'Sport',
            'country': 'Primary Country',
            'is_active': 'Active',
        }
    

# Form to set up the site's details.
class SiteSetupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['site_name', 'site_type']
        labels = {
            'site_name': 'Website Name',
            'site_type': 'Website Type',
        }
    

# Form to set the site's colour scheme.
class SiteColorForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['primary_color', 'primary_text', 'secondary_color', 'secondary_text']
        labels = {
            'primary_text': 'Primary Text Color',
            'primary_color': 'Primary Background Color',
            'secondary_color': 'Secondary Background Color',
            'secondary_text': 'Secondary Text Color',
        }
        widgets = {
            'primary_color': TextInput(attrs={'type': 'color'}),
            'primary_text': TextInput(attrs={'type': 'color'}),
            'secondary_color': TextInput(attrs={'type': 'color'}),
            'secondary_text': TextInput(attrs={'type': 'color'}),
        }
    

# Form to create a new edition of a competition.
class NewEditionForm(forms.ModelForm):
    teams = forms.ModelMultipleChoiceField(queryset=Club.objects.order_by('full_name'))

    class Meta:
        model = Edition
        fields = ['name', 'competition', 'season', 'is_current', 'teams']
        labels = {
            'name': 'Edition Name',
            'competition': 'Competition',
            'season': 'Season',
            'teams': 'Teams',
            'is_current': 'Current Season',
        }
    

# Form to edit an existing edition of a competition.
class EditEditionForm(forms.ModelForm):

    class Meta:
        model = Edition
        fields = ['name', 'competition', 'season', 'is_current']
        labels = {
            'name': 'Edition Name',
            'competition': 'Competition',
            'season': 'Season',
            'is_current': 'Current Season',
        }
    

# Form to create or edit a club.
class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ['full_name', 'short_name', 'abbreviation', 'country', 'logo', 'current_league', 'primary_color', 'primary_text', 'secondary_color', 'secondary_text']
        labels = {
            'full_name': 'Full Name',
            'short_name': 'Short Name',
            'abbreviation': 'Abbreviation',
            'country': 'Country',
            'logo': 'Team Logo',
            'current_league': 'Current League',
            'primary_text': 'Primary Text Color',
            'primary_color': 'Primary Background Color',
            'secondary_color': 'Secondary Background Color',
            'secondary_text': 'Secondary Text Color',
        }
        widgets = {
            'primary_color': TextInput(attrs={'type': 'color'}),
            'primary_text': TextInput(attrs={'type': 'color'}),
            'secondary_color': TextInput(attrs={'type': 'color'}),
            'secondary_text': TextInput(attrs={'type': 'color'}),
        }
    

# Form to create or edit a player.
class PlayerForm(forms.ModelForm):
    current_club = forms.ModelChoiceField(queryset=Club.objects.order_by('full_name'))

    class Meta:
        model = Player
        fields = ['first_name', 'middle_names', 'last_name', 'date_of_birth', 'place_of_birth', 'country', 'current_club']
        labels = {
            'first_name': 'First Name',
            'middle_names': 'Middle Names',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'place_of_birth': 'Place of Birth',
            'country': 'Nationality',
            'current_club': 'Current Club',
        }
        widgets = {
            'date_of_birth': TextInput(attrs={'type': 'date'}),
        }