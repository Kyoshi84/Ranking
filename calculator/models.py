#from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.query_utils import DeferredAttribute

# Create your models here.
class Player(models.Model):
	class Meta:
		verbose_name = _("Gracz")
		verbose_name_plural = _("Gracze")
#	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	name = models.CharField(max_length=50, verbose_name=u"Imię")
	nicname = models.CharField(max_length=50, verbose_name="Pseudonim", blank=True)
	email = models.EmailField(max_length=254, blank=True)


		
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

class Army(models.Model):
	class Meta:
		verbose_name = ("Armia")
		verbose_name_plural = ("Armie")
	name = models.CharField(max_length=100, verbose_name="Nazwa armii")

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

class Tournament(models.Model):
	class Meta:
		verbose_name = _("Turniej")
		verbose_name_plural = _("Turnieje")
	name = models.CharField(max_length=100)
	date = models.DateTimeField('date')
	player_num = models.IntegerField(verbose_name="Liczba graczy")
	points = models.FloatField(default=1000.00)
	rating = models.FloatField(verbose_name="Rating", blank=True)
 #   base_rating = models.DecimalField(decimal_places=3, max_digits=6, default = '0.001', editable=False)
	@property
	def get_rating(self):
		return (self.points) / (1000.00)
	def save(self, *args, **kwargs):
		self.rating = self.get_rating 
		super(Tournament, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
	def __float__(self):
		return self.rating


class TournamentStandings(models.Model):
	class Meta:
		verbose_name = _("Wyniki")
		verbose_name_plural = _("Wyniki")
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)

	army = models.ForeignKey(Army, on_delete=models.CASCADE)
	player_place = models.FloatField(verbose_name=u"Miejsce na turnieju")
	killpoints = models.CharField(verbose_name="Kill points", max_length=9, default='0')
	scenerypoints = models.CharField(verbose_name="Scenariusz", max_length=3, default='0')
	player_points = models.FloatField(verbose_name="Punkty", blank=True)
	
	@property


	def get_player_points(self):
		player_num = float(self.tournament.player_num)
		rating = float(self.tournament.rating)
		player_points = float((rating)*(player_num)- (rating)*(self.player_place -1.00))
##		player_points = ((self.rating)*(self.player_num)- (self.rating)*(self.player_place -1.00))
		return player_points
	def save(self, *args, **kwargs):
		self.player_points = self.get_player_points
		super(TournamentStandings, self).save(*args, **kwargs)

	def __float__(self):
		return self.player_points







class Timeline(models.Model):
	class Meta:
		verbose_name = ("Linia czasu")
		verbose_name_plural = ("Linie czasu")
	
	date = models.DateTimeField('date')
	title = models.CharField(verbose_name=u"Tytuł", max_length=30, default='Tytul')
	info = models.CharField(verbose_name="Informacja", max_length=245, default='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry...')
	#logo = models.ImageField(upload_to = 'documents/%Y/%m/%d')

	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title