# -*- coding: utf-8 -*-
from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
	
	class Meta:
		model = Subscription


	def __init__(self, *args, **kwargs):
		super(SubscriptionForm, self).__init__(*args, **kwargs)

		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['placeholder'] = field_name
