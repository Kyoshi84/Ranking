from .models import Player, Timeline, TournamentStandings, News
#change it before push
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import FormView
from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.template import context
from django.template import RequestContext, Context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Min, Sum, Avg
# Create your views here.

def home(request):
    return render_to_response('home.html')

def kontakt(request):
    return render_to_response('kontakt.html')

def players(request):
    all_players = Player.objects.all().order_by('id')

    return render(request, 'players.html', {'all_players':all_players})

def tournaments(request):
    return HttpResponse("You're looking at Tournaments")

def tournament(request):
    return HttpResponse("You're looking at Single Tournament")

def rankings(request):
# *****working full list of players and their scores *****
# ranking_list = TournamentStandings.objects.all().order_by('player')

# **** working annotate for player__name. Need order by points
# **** ranking_list = TournamentStandings.objects.values('player__name').annotate(Sum('player_points'))

#***** testing date filter
    ranking_list = TournamentStandings.objects.values('player__name').filter(tournament__date__year='2017').annotate(Sum('player_points'))
    return render(request, 'rankings.html', {'ranking_list': ranking_list})

def timeline(request):
    timeline = Timeline.objects.all().order_by('date')

    return render_to_response('timeline.html', {'timeline': timeline})

def news(request):
    news = News.objects.all().order_by('date')
    return render_to_response('news.html', {'news': news})
