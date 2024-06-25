from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(
            request,
            'home.html'
        )


class ContatoView(View):
    def get(self, request):
        return render(
            request,
            'contato.html'
        )


class LocalView(View):
    def get(self, request):
        return render(
            request,
            'local.html'
        )