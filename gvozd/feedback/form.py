from .models import  Message
from django.forms import ModelForm, TextInput, Textarea
from django.forms import ModelForm


class MakeMassage(ModelForm):
    class Meta:
        model = Message
        fields = ('username', 'text')
        labels = {'username': 'Ник:', 'text': 'Сообщение:'}
        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Введите ваш ник',
                'name': 'username',
                'type': 'text', }),
            'text': Textarea(attrs={
                'placeholder': 'Введите ваше сообщение',
                'name': 'text',
                'type': 'text'}),
        }
