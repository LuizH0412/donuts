from donuts.models import Donut
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from centos.models import Cento


class CombinedListView(View):
    def get(self, request, *args, **kwargs):
        donuts = Donut.objects.all()
        centos = Cento.objects.all()
        context = {
            'donuts': donuts,
            'centos': centos,
        }
        return render(request, 'list_donut.html', context)


class DonutListView(ListView):
    model = Donut
    template_name = 'list_donut.html'
    context_object_name = 'list_donut'


    def get_queryset(self):
        donut = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')

        if search:
            donut = donut.filter(icontains__nome=search)
        return donut

class DonutDetailView(DetailView):
    model = Donut
    template_name = 'detail_donut.html'
    context_object_name = 'detail_donut'








