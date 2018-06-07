from django.conf.urls import url, include


from . import views
from .views import ScrollListView

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    #url(r'^warscrolls/', views.warscrolls, name='warscrolls'),
    #url(r'^warscroll/(?P<scroll_id>\d+)/$', views.warscroll, name='warscroll'),
 #   url(r'^players/(?P<player_id>\d+)/$', views.player, name='gracz'),
    url(r'^keywords/', views.keyword, name='keaywords'),
    url(r'^warscrolls/$', ScrollListView.as_view(), name='warscrolls'),


]
