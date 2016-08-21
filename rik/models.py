from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils import timezone
from rik.utils import *

class fyysilineIsik(models.Model):
	isikukood = models.CharField(max_length=11,validators=[MinLengthValidator(11,"Isikukood peab sisaldama ühtteist numbrit; hetkel on %(show_value)d."),onlyNumbers])
	eesnimi = models.CharField(max_length=100,validators=[onlyAlphabet])
	perenimi = models.CharField(max_length=100,validators=[onlyAlphabet])

	def __str__(self):
		return self.eesnimi + " " + self.perenimi

class juriidilineIsik(models.Model):
	regkood = models.CharField(max_length=7,validators=[MinLengthValidator(7,"Registrikood peab sisaldama seitset numbrit; hetkel on %(show_value)d."),onlyNumbers])
	nimi = models.CharField(max_length=100,validators=[MinLengthValidator(3,"Nimi peab sisaldama vähemalt kolme tähte ja/või numbrit; hetkel on %(show_value)d." ),onlyAlphanumerical])

	def __str__(self):
		return self.nimi 

class osayhing(models.Model):
	regkood = models.CharField(max_length=7,validators=[MinLengthValidator(7,"Registrikood peab sisaldama seitset numbrit; hetkel on %(show_value)d."),onlyNumbers])
	nimi = models.CharField(max_length=100,validators=[MinLengthValidator(3,"Nimi peab sisaldama vähemalt kolme tähte ja/või numbrit; hetkel on %(show_value)d." ),onlyAlphanumerical])
	asutamiskp = models.DateField(validators=[validateDate])
	kogukapital = models.IntegerField(validators=[MinValueValidator(2500,"Kogukapitali suurus peab olema vähemalt 2500 eurot.")])

	def __str__(self):
		return self.nimi		

class osanik(models.Model):
	fyysilineIsik = models.ForeignKey(fyysilineIsik, blank=True, null=True)
	juriidilineIsik = models.ForeignKey(juriidilineIsik, blank=True, null=True)
	osayhing = models.ForeignKey(osayhing, blank=True, null=True)
	osakapital = models.IntegerField(validators=[MinValueValidator(1,"Osakapitali suurus peab olema vähemalt 1 eurot.")])
	asutaja = models.BooleanField(default=True)

	def clean(self):
		if self.fyysilineIsik and self.juriidilineIsik:
			raise ValidationError("Osanik ei saa olla juriidiline ja füüsiline isik üheaegselt!")
		if not self.fyysilineIsik and not self.juriidilineIsik:
			raise ValidationError("Osanik on puudu!")

	def __str__(self):
		if self.fyysilineIsik:
			return str(self.fyysilineIsik)
		if self.juriidilineIsik:
			return str(self.juriidilineIsik)









