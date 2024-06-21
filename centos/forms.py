from django import forms
from centos.models import Cento



class CentoModelForm(forms.ModelForm):
    class Meta:
        model = Cento
        fields = '__all__'
    

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')

        if valor <= 0:
            raise forms.ValidationError('O valor não deve ser menor ou igual a zero!')
        return valor