from django import forms
from .models import todomodel

class todoform(forms.ModelForm):
    class Meta:
        model = todomodel
        fields = ['task']
