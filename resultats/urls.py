from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('accueil', views.home, name="accueil"),
    path('race/<int:id_race>', views.race_results, name="race_results"),
    path('race/registrations', views.race_registrations, name="race_registrations"),
    path('connexion', views.connexion, name='connexion'),
    path(r'^deconnexion$', views.deconnexion, name='deconnexion'),
    path('race/registration_form', views.race_registration_form, name='race_registration_form'),
    path('race/list_results_admin/<int:id_race>', views.race_list_results_admin, name='race_list_results_admin'),
    path('race/save_results/<int:id_race>/<int:id_user>', views.race_save_results, name='race_save_results')

]
