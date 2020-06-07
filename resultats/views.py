from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from resultats.models import Race, Runner, RunnerRace
from .forms import ConnexionForm, RunnerRaceForm, SaveRaceResultsForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from datetime import date


@login_required()
def home(request):
    today = date.today()
    races = Race.objects.filter(date__lt=today)
    return render(request, 'resultats/home.html',
        locals())


@login_required()
def race_results(request, id_race):
    today = date.today()
    race = Race.objects.get(id=id_race)
   # runners = race.runners.all('race__runnerrace__time')
    runners = RunnerRace.objects.filter(race=race)
    return render(request, 'resultats/race_results.html', locals())


@login_required()
def race_registrations(request):
    today = date.today()
    runner = Runner.objects.get(id=request.user.id)
    races = runner.race_set.filter(date__gt=today)
    return render(request, 'resultats/race_registrations.html', locals()
                  )


def connexion(request):
    error = False
    user = None
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(home)
            else:
                error = True
    else:
        form = ConnexionForm()

    if user is not None:
        return redirect(home)
    return render(request, 'resultats/login.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


@login_required()
def race_registration_form(request):
    renvoi = False
    runner = Runner.objects.get(id=request.user.id)
    form = RunnerRaceForm(request.POST or None)
    form.fields["runner"].initial = runner
    if form.is_valid():
        form.save()
        return redirect('race_registrations')
    return render(request, 'resultats/form_registration_race.html', locals())
from pprint import pprint

@login_required()
def race_list_results_admin(request, id_race):
    renvoi = False
    race = Race.objects.get(id=id_race)
    return render(request, 'resultats/race_list_results_admin.html', locals())

@login_required()
def race_save_results(request, id_race, id_user):
    renvoi = False
    runner =Runner.objects.get(id = id_user)
    race = Race.objects.get(id = id_race)
    rr = RunnerRace.objects.get(runner = runner, race=race)
    form = SaveRaceResultsForm(request.POST or None, instance=rr)

    if form.is_valid():
       # form.fields["runner"].initial = runner
       # form.fields["race"].initial = race

        form.save()

    return render(request, 'resultats/form_save_results.html', locals())