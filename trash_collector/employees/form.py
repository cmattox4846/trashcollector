from django import forms

class DaysOfWeek(forms.Form):
    day = forms.CharField(widget=forms.Select)