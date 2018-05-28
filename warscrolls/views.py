from .models import Scroll, Keyword
#change it before push
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import FormView
from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.template import context
from django.template import RequestContext, Context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Min, Sum, Avg
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist
from django_tables2 import RequestConfig
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .tables import ScrollTable
from .filters import ScrollListFilter
from .utils import PagedFilteredTableView
from .forms import ScrollListFormHelper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
# Create your views here.

#def warscrolls(request):
#    warscrolls = Scroll.objects.all().order_by('name')

#    return render(request, 'warscrolls.html', {'warscrolls':warscrolls})

def keyword(request):
    keyword = Keyword.objects.all().order_by('name')

    return render(request, 'keywords.html', {'keyword':keyword})

#def warscroll(request):
#    warscroll = Scroll.objects.all().order_by('id')

#    return render(request, 'warscrolls.html', {'warscrolls':warscrolls})



class ScrollListView(PagedFilteredTableView):
    model = Scroll
    template_name = 'scroll_list.html'
    context_object_name = 'scroll'
    ordering = ['-id']
#    group_required = u'company-user'
    table_class = ScrollTable
    filter_class = ScrollListFilter
    formhelper_class = ScrollListFormHelper

    def get_queryset(self):
        qs = super(ScrollListView, self).get_queryset()
        return qs

    def post(self, request, *args, **kwargs):
        return PagedFilteredTableView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super(ScrollListView, self).get_context_data(**kwargs)
        context['nav_scroll'] = True
        search_query = self.get_queryset()
        table = ScrollTable(search_query)
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context
