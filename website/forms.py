from django import forms
from django.forms import ModelForm
from .models import Apptmnts


# Create Appointment Form
class ApptForm(ModelForm):
	class Meta:
		model = Apptmnts
		#fields = "__all__"
		fields = ('client_name', 'therapist_name', 'appt_date', 'room',)

		widgets = {
			'client_name' : forms.Select(attrs={'class':'form-control', 'default':'Client Name'}),
			'appt_date' : forms.HiddenInput(),
			'room' : forms.HiddenInput()

		}

