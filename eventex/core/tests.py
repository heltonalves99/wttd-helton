# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from django.test import TestCase

from apps.subscriptions.forms import SubscriptionForm


class HomeTest(TestCase):

	def setUp(self):
		self.resp = self.client.get('/')
		self.content = pq(self.resp.content)

	def test_get(self):
		"""
			GET / must return status code 200.
		"""

		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		"""
			Home must use template index.html.
		"""

		self.assertTemplateUsed(self.resp, 'index.html')

	def test_csrf(self):
		"""
			Html must contain csrf token.
		"""

		self.assertEqual(1, len(self.content.find('input[name=csrfmiddlewaretoken]')))

	def test_has_form(self):
		"""
			Context must have the subscription form.
		"""

		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	def test_form_has_fields(self):
		"""
			Form must have 4 fields.
		"""

		form = self.resp.context['form']
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)