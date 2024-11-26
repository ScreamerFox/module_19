from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин",
        widget=forms.TextInput(attrs={
            'placeholder': 'Логин',
            'required': True
        })
    )
    password = forms.CharField(
        min_length=8,
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'required': True
        })
    )
    repeat_password = forms.CharField(
        min_length=8,
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
            'required': True
        })
    )
    age = forms.IntegerField(
        max_value=999,
        label="Введите свой возраст",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Возраст',
            'required': True
        })
    )
