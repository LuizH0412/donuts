from centos.models import Cento
from django.views.generic import ListView, DetailView

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


class CentoDetailView(DetailView):
    model = Cento
    template_name = 'detail_cento.html'
    context_object_name = 'detail_cento'

