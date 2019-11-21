from django import forms


class SearchForm(forms.Form):
    full_phone_number = forms.CharField(
        label='Телефонный номер(с кодом)',
        min_length=10, max_length=10)

