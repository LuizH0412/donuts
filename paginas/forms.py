from django import forms
import re

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Seu nome..'
    }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Seu email..'
    }))
    numero = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Seu telefone (XX) XXXX-XXXX'
    }))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Sua mensagem..'
    }))

