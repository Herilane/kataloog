# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.db.models import Q, Sum
from datetime import datetime
from .forms import osayhingForm, osanikForm, fyysilineIsikForm
from .models import osayhing, osanik

def avaleht(request):
	return render(request, 'rik/avaleht.html', {})

def andmed(request, pk):
	oy_andmed = get_object_or_404(osayhing, pk=pk)
	oy_osanikud = osanik.objects.filter(osayhing=oy_andmed)
	return render(request, 'rik/andmed.html', {'oy_andmed': oy_andmed, 'oy_osanikud': oy_osanikud})

def nimekiri(request):
	if 'paring' in request.GET and request.GET['paring']:
		osayhingud = osayhing.objects.filter(Q(nimi__icontains=request.GET['paring'])| Q(regkood=request.GET['paring']))
		return render(request, 'rik/nimekiri.html', {'osayhingud': osayhingud})
	else:
		return redirect('avaleht')

def asutamine(request):
	if request.method == "POST":
		form = osayhingForm(request.POST)
		if form.is_valid(): 
			uus_osayhing = form.save(commit=False)
			uus_osayhing.save()
			return redirect('lisaosanik', pk=uus_osayhing.pk)
	else:
		form = osayhingForm()
	return render(request, 'rik/asutamine.html', {'form': form}) 


def lisaosanik(request, pk):
	pohiandmed = get_object_or_404(osayhing, pk=pk)
	if request.method == "POST":
		form = osanikForm(request.POST)
		if form.is_valid():
			uus_osanik = form.save(commit=False)
			uus_osanik.osayhing = pohiandmed
			uus_osanik.asutaja = True
			uus_osanik.save()
			# Arvuta kokku, kui palju on antud osaühingu osanike osakapitalide summa
			osakapitalid_kokku = osanik.objects.filter(osayhing__pk = pk).aggregate(Sum('osakapital')).get('osakapital__sum')
			kogukapital = osayhing.objects.only('kogukapital').get(pk=pk).kogukapital
			if osakapitalid_kokku < kogukapital:
				message = 'Osanike osakapitalide summa on %s, osaühingu kogukapital on %s. Palun lisa osanik juurde.' % (osakapitalid_kokku, kogukapital)
				return render(request, 'rik/lisaosanik.html', {'form': form, 'message': message})
			else:
				return redirect('andmed', pk=pohiandmed.pk)
	else:
		form = osanikForm()
	return render(request, 'rik/lisaosanik.html', {'form': form})

#TO-DO
def lisafi(request, pk):
	pohiandmed = get_object_or_404(osayhing, pk=pk)
	if request.method == "POST":
		form = fyysilineIsikForm(request.POST)
		if form.is_valid():
			uus_fi = form.save(commit=False)
			uus_fi.save()
			return redirect('lisaosanik', pohiandmed.pk)
	else:
		form = fyysilineIsikFormForm()
	return render(request, 'rik/lisafi.html', {'form': form})



