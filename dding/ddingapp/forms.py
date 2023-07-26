from django import forms
from .models import *

class GongmoForm(forms.ModelForm):
    class Meta:
        model = Gongmo
        fields = ["title"]

class TeamForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    plan_capacity = forms.IntegerField(min_value=0, initial=0, label="기획 인원 수")
    dev_capacity = forms.IntegerField(min_value=0, initial=0, label="개발 인원 수")
    design_capacity = forms.IntegerField(min_value=0, initial=0, label="디자인 인원 수")

    class Meta:
        model = Team
        fields = ["name", "plan_capacity", "dev_capacity", "design_capacity"]

class JickgoonForm(forms.ModelForm):
    class Meta:
        model = Jickgoon
        fields = ['name']