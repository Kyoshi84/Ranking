from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Keyword, Scroll
from calculator.models import Army
from datetime import datetime
from django.db.models import Count, Sum
# Register your models here.


class KeywordResource(resources.ModelResource):
	   class Meta:
            model = Keyword

class ScrollResource(resources.ModelResource):
	   class Meta:
            model = Keyword



class KeywordAdmin(ImportExportModelAdmin):

	list_display = ['id','keyword']
	list_display_links = ['keyword']
	search_fields = ['keyword']

	def name(self, obj):
		return obj.keyword.keyword
		name.short_description = 'Keyword'  #Renames column head

class ScrollAdmin(ImportExportModelAdmin):
	filter_horizontal = ['key']
	list_display = ['id','name', 'army']
	list_display_links = ['name']
	search_fields = ['name', 'army',]
	list_filter = ['army']

	def name(self, obj):
		return obj.warscroll.name
		name.short_description = 'Warscroll'  #Renames column head

# Register your models here.
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Scroll, ScrollAdmin)
