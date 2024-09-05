from django import forms
from portalapp.models import *

class getUserInfo(forms.ModelForm):
	
	class Meta:
		model = alumniInfo
		exclude = ('created_at','updated_at','user')

class eventsForm(forms.ModelForm):
	class Meta:
		model = events
		exclude = ('alumni','posted_on')

class createUser(forms.ModelForm):
	class Meta:
		model = alumniUser
		fields = "__all__"
		


class joblistForm(forms.ModelForm):
	class Meta:
		model = events
		exclude = ('user','status')