from django.conf.urls import url, include


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^timeline/', views.timeline, name='timeline'),
    url(r'^players/', views.players, name='lista_graczy'),
 #   url(r'^players/(?P<player_id>\d+)/$', views.player, name='gracz'),
    url(r'^tournaments/', views.tournaments, name='lista_turnieji'),
    url(r'^tournaments/(?P<tournament_id>\d+)/$', views.tournament, name='turniej'),
    url(r'^rankings2017/', views.rankings2017, name='rankings2017'),
    url(r'^rankings2018/', views.rankings2018, name='rankings2018'),
    url(r'^kontakt/', views.kontakt, name='kontakt'),
    url(r'^news/', views.news, name='news'),

]
