from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import View
from paginas.forms import ContatoForm


class HomeView(View):
    def get(self, request):
        return render(
            request,
            'home.html'
        )

class LocalView(View):
    def get(self, request):
        return render(
            request,
            'local.html'
        )

class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email'] 
        numero = form.cleaned_data['numero'] 
        mensagem = form.cleaned_data['mensagem'] 

        send_mail(
            subject=f'Contato de {nome}',
            message=f'Nome: {nome}\nEmail: {email}\nTelefone: {numero}\n\nMensagem: {mensagem}',
            from_email=email,
            recipient_list=['minidelicias08@gmail.com'],
        )

        return super().form_valid(form)
