from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.views import View
from django.views.generic.edit import FormView
from emails.forms import EmailModelForm
from emails.models import Email


class ContatoView(View):
    def get(self, request):
        return render(
            request,
            'contato.html'
        )



class EmailView(FormView):
    template_name = 'contato.html'
    form_class = EmailModelForm
    success_url= '/contato/'

    def email(self, form):
        nome = form.cleaned_data['nome']
        telefone = form.cleaned_data['telefone']
        email = form.cleaned_data['email']
        assunto = form.cleaned_data['assunto']
        mensagem = form.cleaned_data['mensagem']


        assunto_email = assunto
        mensagem_email = f'Mensagem de {nome}: ({email}) - ({telefone}):\n\n{mensagem}'
        para = settings.DEFAULT_FROM_EMAIL
        destinatarios = ['minidelicias08@gmail.com']


        send_mail(assunto_email, mensagem_email, para, destinatarios)


        return super().form_valid(form)







