from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


#class GsmFilterForm(forms.Form):
#    message = forms.CharField(widget=forms.Textarea, required=True)


class GsmFilterForm(forms.ModelForm):
    class Meta:
        model=GsmFilter
        fields=['text']

    def clean_message(self):
        text= self.cleaned_data.get('text')
        return text
