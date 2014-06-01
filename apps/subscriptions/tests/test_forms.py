# -*- coding: utf-8 -*-
from django.test import TestCase

from apps.subscriptions.forms import SubscriptionForm


class SubscriptionTest(TestCase):
	
	def test_has_fields(self):
			"""
				Form must have 4 fields.
			"""

			form = SubscriptionForm()
			self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)