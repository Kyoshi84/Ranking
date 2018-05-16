from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Keyword, Warscroll
from calculator.models import Army
from datetime import datetime
from django.db.models import Count, Sum
# Register your models here.
class KeywordResources(resources.ModelResource):
	class Meta:
		model = Keyword


class KeywordAdmin(ImportExportModelAdmin):

	list_display = ['id_keyword','keyword']
	list_display_links = ['keyword']
	search_fields = ['keyword']

	def name(self, obj):
		return obj.keyword.keyword
		name.short_description = 'Keyword'  #Renames column head

class WarscrollAdmin(ImportExportModelAdmin):
	filter_horizontal = ['keywords']
	list_display = ['id_user','name', 'army']
	list_display_links = ['name']
	search_fields = ['name', 'army',]
	list_filter = ['army']

	def name(self, obj):
		return obj.warscroll.name
		name.short_description = 'Warscroll'  #Renames column head

# Register your models here.
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Warscroll, WarscrollAdmin)
