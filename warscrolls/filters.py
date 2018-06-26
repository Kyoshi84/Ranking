# filters.py
import django_filters
from .models import Scroll, Keyword
from django import forms


class ScrollListFilter(django_filters.FilterSet):

  class Meta:
    model = Scroll
    fields = {
    'name': ['contains'],
    'key': ['contains'],
    'army': ['exact']
    }
    order_by = ['id']


class WarscrollFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    key = django_filters.ModelMultipleChoiceFilter(queryset=Keyword.objects.all(), widget=forms.CheckboxSelectMultiple)
    #scroll.army__army__name = django_filters.CharFilter(lookup_expr='exact')


    class Meta:
        model = Scroll
        fields = ['id', 'name', 'army', 'key']
