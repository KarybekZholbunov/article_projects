from django import forms
from django.forms import widgets


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    author = forms.CharField(max_length=50, required=False, label="Автор",
                             widget=widgets.TextInput(attrs={'placeholder': 'Автор'}))
    content = forms.CharField(max_length=1000, required=True, label="Контент",
                              widget=forms.Textarea(attrs={"cols": 20, "rows": 8, "placeholder": "Контент"}))