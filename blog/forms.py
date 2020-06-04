from django import forms
from .models import Question


class NewQuestion(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)