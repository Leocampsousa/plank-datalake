from django import forms
from process.models import RaciActivity, RaciRelated


class RaciActivityForm(forms.ModelForm):

    str_title = forms.CharField(
        label='Nome *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    
    str_desc = forms.CharField(
        label='Descricao *',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    CHOICE_COLOR = (
        ('red', 'red'),
        ('green', 'green'),
        ('blue', 'blue')
    )

    str_color = forms.ChoiceField(
        label='cor',
        choices=CHOICE_COLOR,
        widget= forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    class Meta:
        model = RaciActivity
        fields = [
            'str_title',
            'str_desc',
            'responsible',
            'str_color',
            'accountable'
        ]

    
class RaciRelatedForm(forms.ModelForm):

    CHOICES_TYPE = (
        ('CON', 'CON'),
        ('INF', 'INF')
    )
    str_type = forms.ChoiceField(
        label='SETOR:',
        choices=CHOICES_TYPE,
        widget=forms.Select(attrs={'class': 'form-select mt-1'}),
        required=True
    )
    class Meta:
        model = RaciRelated
        fields = [
            'str_type',
            'person'
        ]
    