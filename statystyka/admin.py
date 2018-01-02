# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Press, Partia
from datetime import datetime
from django.db.models import Count, Sum

# Register your models here.
class PressAdmin(admin.ModelAdmin):

	list_display = ['title', 'owner',]
	list_display_links = ['title']


	def name(self, obj):
		return obj.press.name
		name.short_description = u'Tytuł' 

class PartiaAdmin(admin.ModelAdmin):
	list_display = ['name', 'fullname']
	list_display_links = ['name']
	
	def name(self, obj):
		return obj.partia.name
		name.short_description = 'Ugrupowanie'
		

admin.site.register(Press, PressAdmin)
admin.site.register(Partia, PartiaAdmin)