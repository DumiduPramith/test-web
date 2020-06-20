from django import forms
from .models import Question


class NewQuestion(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    question_image = forms.ImageField(required=False)