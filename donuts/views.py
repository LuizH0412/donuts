from donuts.models import Donut
from django.shortcuts import render
from donuts.forms import DonutModelForm
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.views import View
from django.urls import reverse_lazy
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


class DonutCreateView(CreateView):
    model = Donut
    form_class = DonutModelForm
    template_name = 'create_donut.html'
    success_url = '/donuts/'


class DonutDetailView(DetailView):
    model = Donut
    template_name = 'detail_donut.html'
    context_object_name = 'detail_donut'


class DonutDeleteView(DeleteView):
    model = Donut
    template_name = 'delete_donut.html'
    success_url = '/donuts/'


class DonutUpdateView(UpdateView):
    model = Donut
    form_class = DonutModelForm
    template_name = 'update_donut.html'


    def get_success_url(self):
        return reverse_lazy('detail_donut', kwargs={'pk': self.objects.pk})





