# -*- coding: utf-8 -*-
from django import forms
from .models import osayhing, osanik, fyysilineIsik
from django.template.loader import render_to_string

class SelectWithPop(forms.Select):
	def render(self, name, *args, **kwargs):
		html = super(SelectWithPop, self).render(name, *args, **kwargs)
		popupplus = render_to_string("blog/popupplus.html", {'field': name})
		return html+popupplus

class osayhingForm(forms.ModelForm):

	asutamiskp = forms.DateField(label='Asutamise kuupäev',help_text='Formaat: yyyy-mm-dd, stiilis "2015-03-01"')

	class Meta:
		model = osayhing
		fields = ('regkood','nimi','kogukapital','asutamiskp')
		labels = {'regkood': "Registrikood",
		'nimi': "Osaühingu nimi",
		'kogukapital': "Kogukapital"}

class osanikForm(forms.ModelForm):

	class Meta:
		model = osanik
		fields = ('fyysilineIsik','juriidilineIsik','osakapital')
		labels = {'fyysilineIsik': "Füüsiline isik", 'juriidilineIsik': "Juriidiline isik",
		'osakapital': "Osakapital"}

class fyysilineIsikForm(forms.ModelForm):

	class Meta:
		model = fyysilineIsik
		fields = ('isikukood','eesnimi','perenimi')
		labels = {'isikukood': "Isikukood",
		'eesnimi': "Eesnimi",
		'perenimi': "Perenimi"}
