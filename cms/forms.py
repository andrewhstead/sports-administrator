from django import forms
from users.models import User
from data.models import Competition
from django.core.exceptions import ValidationError


# Simple username and password login.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

# Form to create a new competition.
class NewCompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ['name', 'sport', 'country']
        labels = {
            'name': 'Competition Name',
            'sport': 'Sport',
            'country': 'Primary Country',
        }
    

# Form to create a new competition.
class EditCompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ['name', 'sport', 'country', 'is_active']
        labels = {
            'name': 'Competition Name',
            'sport': 'Sport',
            'country': 'Primary Country',
            'is_active': 'Active',
        }
    

# Form to create a new competition.
class ConfigurationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['site_name', 'site_type']
        labels = {
            'site_name': 'Website Name',
            'site_type': 'Website Type',
        }