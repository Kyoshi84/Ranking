#from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.query_utils import DeferredAttribute

# Create your models here.

class Keyword(models.Model):
    class Meta:
        verbose_name = ("Keyword")
        verbose_name_plural = ("keywords")
    keyword = models.CharField(max_length=25)
    def __str__(self):
        return self.keyword
    def __unicode__(self):
        return self.keyword



class Scroll(models.Model):
    class Meta:
        verbose_name = ("Warscroll")
        verbose_name_plural = ("Warscrolls")
    name = models.CharField(max_length=50, verbose_name=u"Nazwa", )
    army = models.ForeignKey('calculator.Army', on_delete=models.CASCADE)
    key = models.ManyToManyField(Keyword)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
