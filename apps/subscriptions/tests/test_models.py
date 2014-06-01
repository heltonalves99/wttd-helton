# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from model_mommy import mommy

from apps.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
	
	def setUp(self):
		self.obj = mommy.make(Subscription)

	def test_create(self):
		"""
			Subscription must have name, cpf, email and phone.
		"""

		self.obj.save()
		self.assertEqual(1, self.obj.pk)

	def test_has_created_at(self):
		"""
			Subscription must have automatic created_at.
		"""

		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)


class SubscriptionUniqueTest(TestCase):

	def setUp(self):
		self.obj = mommy.make(Subscription, name="helton alves", cpf="12345678901", email="admin@admin.com.br")
		self.obj.save()

	def test_cpf_unique(self):
		"""
			CPF must be unique.
		"""	

		obj = mommy.make(Subscription)
		obj.cpf = "12345678901"
		self.assertRaises(IntegrityError, obj.save)

	def test_email_unique(self):
		"""
			Email must be unique.
		"""	

		obj = mommy.make(Subscription)
		obj.email = "admin@admin.com.br"
		self.assertRaises(IntegrityError, obj.save)

	def test_unicode(self):
		self.assertEqual("helton alves", unicode(self.obj))