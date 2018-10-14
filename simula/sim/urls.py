from django.contrib import admin
from django.urls import path

from . import views 

urlpatterns = [ 
    
    path('accueil' , views.accueil , name="accueil"),
    path('apropos' ,views.apropos , name="apropos" ),
    path('telechargement' ,views.telechargement , name="telechargement" ),
    path('communaute' ,views.communaute , name="communaute" ),
    path('galerie' ,views.galerie , name="galerie" ),
    path('documentation_simula' ,views.documentation_simula , name="documentation_simula" ),
    path('forum' ,views.forum , name="forum" ),
    path('exercices_corrige' ,views.exercices_corrige , name="exercices_corrige" ),
    path('contact' ,views.contact , name="contact" ),
    path('donate' ,views.donate , name="donate"),
    path('donate_card' ,views.donate_card , name="donate_card"),

    


]
