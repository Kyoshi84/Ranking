from django.conf.urls import url, include


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^timeline/', views.timeline, name='timeline'),
    url(r'^players/', views.players, name='lista_graczy'),
    url(r'^players/(?P<player_id>\d+)/$', views.player, name='gracz'),
    url(r'^tournaments/', views.tournaments, name='lista_turnieji'),
    url(r'^tournaments/(?P<tournament_id>\d+)/$', views.tournament, name='turniej'),
    url(r'^rankings/', views.rankings, name='rankings'),
    url(r'^kontakt/', views.kontakt, name='kontakt'),

]

