# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from django.test import TestCase
from model_mommy import mommy

from apps.subscriptions.forms import SubscriptionForm
from apps.subscriptions.models import Subscription


class SubscriptionsTest(TestCase):

	def setUp(self):
		self.resp = self.client.get('/inscription/')
		self.content = pq(self.resp.content)

	def test_get(self):
		"""
			GET /inscription/ must return status 200.
		"""

		self.assertEqual(200, self.resp.status_code)

	def test_html(self):
		"""
			Html must contain input controls.
		"""

		self.assertTrue(self.content.is_('form'))
		self.assertEqual(6, len(self.content.find('input')))
		self.assertEqual(3, len(self.content.find('input[type=text]')))
		self.assertEqual(1, len(self.content.find('input[type=email]')))
		self.assertEqual(1, len(self.content.find('input[type=submit]')))

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


class SubscriptionsPostTest(TestCase):

	def setUp(self):
		data = dict(name="helton alves", cpf='1231231231',
					email="helton@admin.com.br", phone="99-81103480")
		self.resp = self.client.post('/inscription/', data)

	def test_post(self):
		"""
			Valid POST should redirect to /inscription/1/.
		"""

		self.assertEqual(302, self.resp.status_code)

	def test_save(self):
		"""
			Valid POST must be saved.
		"""

		self.assertTrue(Subscription.objects.exists())


class SubscriptionsInvalidPostTest(TestCase):

	def setUp(self):
		data = dict(name="helton alves", cpf='000000000012',
					email="helton@admin.com.br", phone="99-81103480")
		self.resp = self.client.post('/inscription/', data)

	def test_post(self):
		"""
			Ivalid POST should not redirect.
		"""

		self.assertEqual(200, self.resp.status_code)

	def test_form_errors(self):
		"""
			Form must contain errors.
		"""

		self.assertTrue(self.resp.context['form'].errors)

	def test_dont_save(self):
		"""
			Do not save data.
		"""

		self.assertFalse(Subscription.objects.exists())


class SubscriptionDetailTest(TestCase):

	def setUp(self):
		self.obj = mommy.make(Subscription)
		self.obj.save()

		self.resp = self.client.get('/inscription/{}/'.format(self.obj.pk))

	def test_get(self):
		"""
			GET /inscription/1/ sould return status 200.
		"""

		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		"""
			Uses template.
		"""

		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

	def test_context(self):
		"""
			Context must have a subscription instance.
		"""

		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)

	def test_html(self):
		"""
			Check if subscription data has rendered.
		"""
		
		self.assertContains(self.resp, self.obj.name)


class DetailNotFound(TestCase):

	def test_not_found(self):
		response = self.client.get('/inscription/0/')
		self.assertEqual(404, response.status_code)