from django.forms import ModelForm
from .models import Crud
from django import forms

class crudForm(ModelForm):
    class Meta:
        model = Crud
        fields = ['content']