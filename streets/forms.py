from django import forms
from .models import Street

class StreetSearchForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='Название улицы')
    house = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='Номер дома')

    class Meta:
        model = Street
        fields = ('name',)
