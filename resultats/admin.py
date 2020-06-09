from django.contrib import admin
from .models import Race, RaceType, RunnerRace, Runner
from django.utils.text import Truncator

class RaceAdmin(admin.ModelAdmin):
    list_display   = ('name', 'city', 'date', 'apercu_contenu')
    list_filter    = ('name','city','type')
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('name', 'city')

    def apercu_contenu(self, race):

        return Truncator(race.address).chars(30, truncate='...')
    apercu_contenu.short_description = 'Aperçu du contenu'
# Register your models here.
admin.site.register(RaceType)
admin.site.register(Race, RaceAdmin)
admin.site.register(RunnerRace)
admin.site.register(Runner)

