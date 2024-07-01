from emails.models import Email
from django import forms


class EmailModelForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'