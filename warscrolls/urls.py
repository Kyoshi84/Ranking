from django.conf.urls import url, include


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^warscrolls/', views.warscrolls, name='warscrolls'),
    url(r'^warscroll/(?P<player_id>\d+)/$', views.warscroll, name='warscroll'),
 #   url(r'^players/(?P<player_id>\d+)/$', views.player, name='gracz'),
    url(r'^keywords/', views.keywords, name='keaywords'),


]
