from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        return f'{name.upper()}'

    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'email', 'date', 'time', 'count', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Ваше ім\'я',
                                           'data-rule': 'minlen:4'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш номер телефону',
                                            'id': 'email', 'data-rule': 'email'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата бронювання'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Час бронювання'}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Кількість осіб'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Коментар'}),
        }
        labels = {
            'name': 'Ім\'я',
            'phone': 'Телефон',
            'email': 'Email',
            'date': 'Дата',
            'time': 'Час',
            'count': 'Кількість',
            'comment': 'Коментар',
        }
        help_texts = {
            'phone': 'Введіть номер телефону у форматі +380XXXXXXXXX',
        }
        error_messages = {
            'name': {
                'required': 'Це поле є обов\'язковим',
            },
            'phone': {
                'required': 'Це поле є обов\'язковим',
            },
            'email': {
                'required': 'Це поле є обов\'язковим',
            },
            'date': {
                'required': 'Це поле є обов\'язковим',
            },
            'time': {
                'required': 'Це поле є обов\'язковим',
            },
            'count': {
                'required': 'Це поле є обов\'язковим',
            },
        }