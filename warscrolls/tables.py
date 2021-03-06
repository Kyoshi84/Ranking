import django_tables2 as tables
from django_tables2.utils import A
from .models import Scroll, Keyword


class ScrollTable(tables.Table):
    #id = tables.LinkColumn('scroll-detail', args=[A('pk')])
    #name = tables.LinkColumn('scroll-detail', args=[A('pk')])
    #army = tables.LinkColumn('scroll-detail', args=[A('pk')])
    #key = tables.LinkColumn('scroll-detail', args=[A('pk')])
    class Meta:
        model = Scroll
#      fields = ('scroll_id', 'scroll_name', 'army','key')
        fields = ('id', 'name', 'army','key')
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no Warscrolls matching the search criteria..."
