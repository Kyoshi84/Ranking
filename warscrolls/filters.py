# filters.py
import django_filters
from .models import Scroll


class ScrollListFilter(django_filters.FilterSet):

  class Meta:
    model = Scroll
    fields = ['id', 'name', 'army','key']
    order_by = ['id']
