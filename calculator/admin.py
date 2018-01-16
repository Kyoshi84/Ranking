#from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Player, Tournament, TournamentStandings, Army, Timeline, News
from datetime import datetime
from django.db.models import Count, Sum


class PlayerResource(resources.ModelResource):
	class Meta:
		model = Player

class TournamentStandingsResource(resources.ModelResource):
	class Meta:
		model = TournamentStandings
		fields = ('id', 'tournament', 'player.id' ,'player', 'player_points', 'killpoints', 'scenerypoints', )

class ArmyResources(resources.ModelResource):
	class Meta:
		model = Army

		

class PlayeryAdmin(ImportExportModelAdmin):

	list_display = ['id','name', 'nicname', 'email']
	list_display_links = ['name']
	search_fields = ['id','name', 'nicname', 'email']
	list_filter = ['name', 'nicname', 'email']

	def name(self, obj):
		return obj.player.name
		name.short_description = 'Imię'  #Renames column head

class TournamentAdmin(ImportExportModelAdmin):

	list_display = ['id','name', 'date', 'player_num', 'points', 'rating']
	list_display_links = ['id','name']
	search_fields = ['name','player_num', 'points']
	list_filter = ['name', 'date', 'player_num', 'points']
	readonly_fields = ['get_rating']
	fields = ['name', 'date', 'player_num', 'points', 'get_rating']





	def name(self, obj):
		return obj.tournament.name
		name.short_description = 'Nazwa turnieju'  #Renames column head

class ArmyAdmin(ImportExportModelAdmin):
	list_display = ['id','name']
	list_display_links = ['name']

	def name(self, obj):
		return obj.army.name
		name.short_description = 'Nazwa armii'

class TournamentStandingsAdmin(ImportExportModelAdmin):

	list_display = ['tournament_name', 'player_id','player_name', 'army' , 'player_place', 'player_points', 'killpoints']
	list_display_links = ['tournament_name']
	search_fields = ['tournament_name', 'player__name']
	list_filter = ['tournament__name', 'player__name']


	def player_name(self, obj):
		return obj.player.name
	def player_id(self, obj):
		return obj.player_id


	def tournament_name(self, obj):
		return obj.tournament.name
		tournament_name.admin_order_field  = 'name'  #Allows column order sorting
		tournament_name.short_description = 'Nazwa turnieju'  #Renames column head
    




class TimelineAdmin(ImportExportModelAdmin):
	list_display = ['date','title']
	list_display_links = ['title']
	search_fields = ['date','title','info']
	list_filter = ['date']

	def name(self, obj):
		return obj.timeline.title

class NewsAdmin(ImportExportModelAdmin):
	list_display = ['date','fblink']
	list_display_links = ['date']
	list_filter = ['date']

	def name(self, obj):
		return obj.news.id
		


	
	




# Register your models here.
admin.site.register(Army, ArmyAdmin)
admin.site.register(Player, PlayeryAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(TournamentStandings, TournamentStandingsAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(News, NewsAdmin)
