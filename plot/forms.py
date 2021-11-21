from django import forms
from .models import Plot, Methods
from django.core.validators import MaxValueValidator, MinValueValidator


class PlotForm(forms.Form):
    method = forms.ModelChoiceField(
        empty_label='choose a method', queryset=Methods.objects.all(), widget=forms.Select(attrs={'class': "form-control"}))
    function = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "x**2"}))
    start = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "inf"}))
    end = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "inf"}))
    split = forms.IntegerField(
        min_value=0, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "0-inf"}))
