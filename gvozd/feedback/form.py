from .models import Message, Favour
from django.forms import ModelForm, TextInput, Textarea, ChoiceField, Select
from django.forms import ModelForm


class MakeMassage(ModelForm):
    class Meta:
        model = Message
        fields = ('username', 'favour', 'text')
        labels = {'username': 'Ник:', 'text': 'Сообщение:','favour': 'f_id'}
        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Введите ваш ник',
                'name': 'username',
                'type': 'text', }),
            'favour' : Select(attrs={'size': 1}),
            'text': Textarea(attrs={
                'placeholder': 'Введите ваше сообщение',
                'name': 'text',
                'type': 'text'}),
        }
