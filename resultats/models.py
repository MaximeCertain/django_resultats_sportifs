from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class RaceType(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Type de course"
    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la course")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de la course")
    city = models.CharField(max_length=100, verbose_name="ville de la course")
    address = models.CharField(max_length=100, verbose_name="Lieu du départ de la course")
    type = models.ForeignKey('RaceType', on_delete=models.CASCADE, default=0)
    runners = models.ManyToManyField("Runner", through='RunnerRace')
    class Meta:
        verbose_name = "Course"
        ordering = ['date']
    def __str__(self):
        return self.name

class Runner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    age = models.IntegerField(verbose_name="Age du coureur")
    registerDate = models.DateTimeField(default=timezone.now, verbose_name="Date d'Inscription")
    class Meta:
        verbose_name = "Coureur"
    def __str__(self):
        return "Profil de {0}".format(self.user.username)

class RunnerRace(models.Model):
    runner = models.ForeignKey(Runner, on_delete=models.PROTECT, verbose_name="Coureur")
    race = models.ForeignKey(Race, on_delete=models.PROTECT, verbose_name="Course")
    registerDate = models.DateTimeField(default=timezone.now, verbose_name="Date d'Inscription à la course")
    indications = models.TextField(max_length=100, verbose_name="Indications spécifiques avant course", default="", null=True)
    time = models.FloatField(verbose_name="temps de course pour ce coureur", default=0)
    bibNumber = models.IntegerField(verbose_name="Numéro de dossard du coureur", default=0)
    class Meta:
        unique_together = ['runner', 'race']

