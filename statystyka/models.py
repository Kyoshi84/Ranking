#from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _

from django.db import models

# Create your models here.
class Press(models.Model):
	class Meta:
		verbose_name = _("Tytul gazety")
		verbose_name_plural = _("Tytuly gazet")
	title = models.CharField(primary_key=True, max_length=50, verbose_name=u"Tytuł")
	owner = models.CharField(max_length=50, verbose_name="Wydawca", blank=True)
	
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

class Partia(models.Model):
	class Meta:
		verbose_name = _("Ugrupowanie")
		
	name = models.CharField(primary_key=True, max_length=10, verbose_name=u"Nazwa")
	fullname = models.CharField(max_length=50, verbose_name=u"Pełna nazwa", blank=True)

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	