from django import forms
from .models import Problem

class AddRecordForm(forms.ModelForm):
    leado_neve = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Hiba leadó neve", "class":"form-control"}), label="")
    hardware_vagy_szotver_hiba = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Hiba jellege Hardware/ Szoftver", "class":"form-control"}), label="")
    rovid_leiras = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Hiba rövid leírása", "class":"form-control"}), label="")
    prioritasa = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Hiba prioritása", "class":"form-control"}), label="")

    class Meta:
        model = Problem
        exclude = ("user", )