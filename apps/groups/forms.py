__author__ = 'MatthewHan'
from django import forms
from .models import Organization
class OrgForm(forms.Form):
    name = forms.CharField(min_length=6)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),min_length=11)
    class Meta:
        model = Organization
