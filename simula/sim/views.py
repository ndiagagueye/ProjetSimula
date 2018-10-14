from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.core.mail import BadHeaderError, EmailMessage

import pypandoc

# Create your views here.
from simula import settings

import os
def detect_os(request):
	if(request.Windows):
		return "Windows"
	if(request.Linux):
		return "Linux"
	else:
		return "Mac"

def derniere_version(request):
	logiciels = Logiciel.objects.all()
	max__first_indice = max__last_indice = 0
	for logiciel in logiciels:
		indice = logiciel.version.version.split('.')
		first_indice = int(indice[0])
		if(first_indice>max__first_indice):
			max_first_indice = first_indice
		last_indice = int(indice[1])
		if(last_indice > max__last_indice and first_indice == max_first_indice):
			max_last_indice = last_indice
	return str(max_first_indice)+"."+str(max__last_indice)

def isVersionTest(request):
	if(Logiciel.objects.filter(version=Version.objects.get(version=derniere_version(request) , status=None))):
		return False
	return True



def infosLastVersion(request):
	last_version = derniere_version(request)
	beta = "beta"
	syste = detect_os(request)
	systeme = Systeme.objects.get(nom=syste)
	if(isVersionTest(last_version)):
		version = Version.objects.get(version=last_version, status=beta)
		version_view = last_version+"."+beta
	else:
		version_view = last_version
		version = Version.objects.get(version=last_version, status=None)
	return {"last_version":last_version ,  "version_view":version_view , "syste":syste ,"version":version}
 

def lastLogiciels(request):
	infosVersion = infosLastVersion(request)
	logiciel32 = logiciel64 = Logiciel.objects.none()
	if(Logiciel.objects.filter(version=infosVersion['version'], systeme__nom=infosVersion['syste'], architecture__nom="64bits")):
		logiciel64 = Logiciel.objects.get(version=infosVersion['version'], systeme__nom=infosVersion['syste'], architecture__nom="64bits")
	if(Logiciel.objects.filter(version=infosVersion['version'], systeme__nom=infosVersion['syste'], architecture__nom="32bits")):
		logiciel32 = Logiciel.objects.get(version=infosVersion['version'], systeme__nom=infosVersion['syste'], architecture__nom="32bits")
	return {"logiciel32":logiciel32, "logiciel64": logiciel64}



	

def accueil(request):
	infosVersion = infosLastVersion(request)
	lastLogiciel = lastLogiciels(request)
    
	return render(request , "sim/accueil.html" , locals())



def apropos(request):
	return render(request , "sim/apropos.html" , locals())




def telechargement(request):
	lastLogiciel = lastLogiciels(request)
	infosVersion = infosLastVersion(request)
	logiciels64l = Logiciel.objects.filter(architecture__nom="64bits", systeme__nom="Linux").order_by('-date')
	logiciels32l = Logiciel.objects.filter(architecture__nom="32bits", systeme__nom="Linux")
	logiciels64w = Logiciel.objects.filter(architecture__nom="64bits", systeme__nom="Windows" ).order_by('-date')
	logiciels32w = Logiciel.objects.filter(architecture__nom="32bits", systeme__nom="Windows")
	logiciels64m = Logiciel.objects.filter(architecture__nom="64bits", systeme__nom="Mac").order_by('-date')
	logiciels32m = Logiciel.objects.filter(architecture__nom="32bits", systeme__nom="Mac")
	return render(request , "sim/telechargement.html" , locals())





def galerie(request):
	image = 'branding'
	return render(request , "sim/galerie.html" , locals())	

def communaute(request):
	return render(request , "sim/communaute.html" , locals()) 

def documentation_simula(request):
	return render(request , "sim/documentation_simula.html" , locals()) 	


def forum(request):
	return render(request , "sim/forum.html" , locals()) 

def exercices_corrige(request):
	return render(request , "sim/exercices_corrige.html" , locals()) 

def donate(request):
	return render(request , "sim/donate.html" , locals())			

def donate_card(request):
	return render(request , "sim/donate_card.html" , locals()) 			


def contact(request):
	if(request.POST):
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']

		email = EmailMessage('Message de '+name+' <'+email+'> ', message, email , ['douss.sy@gmail.com'])
		email.send()
		send = True 
	
	return render(request , "sim/contact.html" , locals()) 		











"""

#Creer une table 
NB: Seul l'administrateur du site aurra la possibilité d'ajouter ou de modifier 
	version : Sumila 1.0 
	systeme : windows (un select)
	architecture : 32bits(un select)










#Posibilité de téléchargement 
<a href="lien/du/fichier" download> telecharger </a>

"""
