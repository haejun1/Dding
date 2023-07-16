from django import forms
from .models import *

class GongmoForm(forms.ModelForm):
    class Meta:
        model = Gongmo
        fields = ["title"]

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["name"]

class JickgoonForm(forms.ModelForm):
    class Meta:
        model = Jickgoon
        fields = ['name']
