# filters.py
import django_filters
from .models import Scroll


class ScrollListFilter(django_filters.FilterSet):

  class Meta:
    model = Scroll
    fields = {
    'name': ['contains'],
    'key': ['contains'],
    'army': ['exact'],
    }
    order_by = ['id']


#'price': ['lt', 'gt'],
