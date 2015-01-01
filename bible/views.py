from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
import datetime
from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
from models import Reading, UserProfile
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext

def initdb(request):
	for x in range(0, 365):
		f = open("bible/parsebible/days/"+str(x), "r")
		verses = f.read()

		reading = Reading(day= x, verse= verses)
		reading.save()
	
	return HttpResponse("db initialized")

def daily(request):
	#default start date is January 1, of current year
	logged_in = False
	this_year = datetime.date.today().year	
	start_date = date(this_year, 1, 1)
	#If a user is logged in check their start date#
	if request.user.is_authenticated():
		logged_in = True
		user_obj = User.objects.get(username=request.user.username) #Get user in users table
		user_prof = UserProfile.objects.get(user_id=user_obj.id) #Get user profile from user
		start_date = user_prof.startDate #Get start date
	#Compare start date to today to get current day
	today = datetime.date.today()
	delta = today - start_date
	verse_day = delta.days
	
	reading = Reading.objects.filter(day=verse_day)[0] #Not sure why 0 element is verse????#
	return render(request, 'daily.html', {'reading': reading, 'day': verse_day, 'logged': logged_in})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_profile = UserProfile(user=new_user, day=0)
			new_profile.save()
			return HttpResponseRedirect("/daily/")
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html",  {'form': form,})




