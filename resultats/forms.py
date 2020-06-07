from django import forms
from resultats.models import Runner, RunnerRace, Race

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class RunnerRaceForm(forms.ModelForm):
    class Meta:
        model = RunnerRace
        fields = ('runner','race','indications')
        widgets = {'runner':forms.HiddenInput()}

class SaveRaceResultsForm(forms.ModelForm):
    class Meta:
        model = RunnerRace
        fields = ['time', 'bibNumber']
