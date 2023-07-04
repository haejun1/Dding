from django import forms
from .models import Gongmo, Team

class GongmoForm(forms.ModelForm):
    class Meta:
        model = Gongmo
        fields = ["title"]

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["name"]