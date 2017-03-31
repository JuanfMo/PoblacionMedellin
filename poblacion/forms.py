from django import forms
from django.forms import ModelForm
from .models import Poblacion


elegiredad =(
    ('0-14', '0-14'),
    ('15-24', '15-24'),
    ('25-34', '25-34'),
    ('35-54', '35-54'),
    ('55-80', '55-80'),
    ('80 y mas', '80 y mas'),
)
elegirano =(
    ('2011', '2011'),
    ('2015', '2015'),
)

class PoblacionForm(forms.ModelForm):

    comuna = forms.CharField()

    edad = forms.ChoiceField(choices=elegiredad)

    poblacion_año = forms.ChoiceField(choices=elegirano)

    numero_poblacion = forms.IntegerField()

    class Meta:
        model = Poblacion
        fields = ['comuna', 'edad', 'poblacion_año', 'numero_poblacion']
