from django.shortcuts import render, redirect
from data.models import Sport, Country, Competition
from django.template.context_processors import csrf
from django.contrib import auth, messages
from django.urls import reverse
from .forms import LoginForm

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
    
    
def new_competition(request):
    
    return render(request, "new_competition.html")