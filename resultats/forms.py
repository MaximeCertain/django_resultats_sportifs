from django import forms
from resultats.models import Runner, RunnerRace, Race, User
from django.contrib.auth.forms import UserCreationForm
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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Nom')
    last_name = forms.CharField(max_length=100, help_text='Prénom')
    email = forms.EmailField(max_length=150, help_text='Email')
    age = forms.IntegerField(help_text='Age du coureur')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'age')