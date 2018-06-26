from django.conf.urls import url, include


from . import views
from .views import ScrollListView
from .filters import ScrollListFilter, WarscrollFilter
from django_filters.views import FilterView

urlpatterns = [
    # url(r'^$', views.home, name='home'),
#    url(r'^warscrolls/', ScrollListView.as_view(), name='warscrolls'),
    #url(r'^warscroll/(?P<scroll_id>\d+)/$', views.warscroll, name='warscroll'),
 #   url(r'^players/(?P<player_id>\d+)/$', views.player, name='gracz'),
    url(r'^keywords/', views.keyword, name='keaywords'),
    url(r'^warscrolls/$', ScrollListView.as_view(filter_class=ScrollListFilter,
        	template_name='scroll_list.html'), name='warscrolls'),
    url(r'^search/$', FilterView.as_view(filterset_class=WarscrollFilter,
        template_name='warscrolls_list.html'), name='search'),


]
