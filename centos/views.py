from centos.models import Cento
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from centos.forms import CentoModelForm


class CentoListView(ListView):
    model = Cento
    template_name = 'list_donut.html'
    context_object_name = 'centos'
    


    def get_queryset(self):
        cento = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')

        if search:
            cento = cento.filter(icontains__valor=search)
        return cento


class CentoCreateView(CreateView):
    model = Cento
    form_class = CentoModelForm
    template_name = 'create_cento.html'
    success_url = '/centos/'



class CentoUpdateView(UpdateView):
    model = Cento
    form_class = CentoModelForm
    template_name = 'update_cento.html'


    def get_success_url(self):
        return reverse_lazy('detail_cento', kwargs={'pk': self.objects.pk})


class CentoDetailView(DetailView):
    model = Cento
    template_name = 'detail_cento.html'
    context_object_name = 'detail_cento'


class CentoDeleteView(DeleteView):
    model = Cento
    template_name = 'delete_cento.html'
    context_object_name = 'delete_cento'

