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

    def clean_numero(self):
        telefone = self.cleaned_data['numero']
        
        telefone_regex = re.compile(r'^\(?\d{2}\)?\s?\d{4,5}-\d{4}$')

        if not telefone_regex.match(telefone):
            raise forms.ValidationError('Número de telefone inválido. Formato esperado: (XX) XXXX-XXXX ou (XX) XXXXX-XXXX')

        return telefone