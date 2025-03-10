from .models import *
from django import forms
from django.forms import ModelForm


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'