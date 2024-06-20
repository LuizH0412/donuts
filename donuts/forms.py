from django import forms
from donuts.models import Donut

class DonutModelForm(forms.ModelForm):
    class Meta:
        model = Donut
        fields = '__all__'