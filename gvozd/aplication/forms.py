from .models import Favour, Aplications
from django.forms import ModelForm, TextInput, Textarea

class FavourForm(ModelForm):
    class Meta:
        model = Favour
        fields = ['name','price']

        widgets = {
            "name":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "price":TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            })
        }