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
        verbose_name = _("Keyword")
        verbose_name_plural = _("keywords")
    id_keyword = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=25, blank=True)
    def __str__(self):
        return self.keyword



class Warscroll(models.Model):
    class Meta:
        verbose_name = ("Warscroll")
        verbose_name_plural = ("Warscrolls")
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name=u"Nazwa")
    army = models.ForeignKey('calculator.Army', on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword)
