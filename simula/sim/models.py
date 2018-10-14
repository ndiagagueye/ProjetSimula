from django.db import models

# Create your models here.

class Systeme(models.Model):
	nom = models.CharField(max_length=100 , verbose_name="Systeme")

	def __str__(self):
		return self.nom




class Architecture(models.Model):
	nom = models.CharField(max_length=100 , verbose_name="Architecture")

	def __str__(self):
		return self.nom


class Version(models.Model):
	version = models.CharField(max_length=10)
	status = models.CharField(max_length=10 , null=True, blank=True )
	def name(self):
		if(self.status):
			return self.version+"."+self.status
		return self.version

	def __str__(self):
		return self.name()

	def versionDownload(self):
		return str("-".join(str(self.name()).split('.')[0:]))


class Logiciel(models.Model):
	systeme = models.ForeignKey(Systeme , on_delete=models.CASCADE)
	architecture = models.ForeignKey(Architecture , on_delete=models.CASCADE)
	logiciel = models.FileField(upload_to="logiciel")
	version = models.ForeignKey(Version, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=False, auto_now_add=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return "Simula"+self.version.name()+" "+self.systeme.nom+" "+self.architecture.nom


	def extension(self):
		return str(".".join(str(self.logiciel.url).split('.')[1:]))