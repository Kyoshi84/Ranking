import django_tables2 as tables
from django_tables2.utils import A
from .models import Scroll


class ScrollTable(tables.Table):
 # scroll_id = tables.LinkColumn('scroll-detail', args=[A('pk')])
  #scroll_name = tables.LinkColumn('scroll-detail', args=[A('pk')])
  #scroll_army = tables.LinkColumn('scroll-detail', args=[A('pk')])
  #scroll_key = tables.LinkColumn('scroll-detail', args=[A('pk')])

  class Meta:
      model = Scroll
#      fields = ('scroll_id', 'scroll_name', 'army','key')
      fields = ('id', 'name', 'army','key')
      attrs = {"class": "table-striped table-bordered"}
      empty_text = "There are no Warscrolls matching the search criteria..."
