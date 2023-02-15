from django import forms
from .models import *
class Comment(forms.ModelForm):
    stars = forms.DecimalField(label="",
      widget=forms.NumberInput(attrs={
        "class":"rating",
        "max": "5",
        "oninput":"this.style.setProperty('--value', `${this.valueAsNumber}`)",
        "step":"1",
    "type":"range",
      "min":"1",
    "value":"1",
        "required":True,
      })
    )
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            "class": "searchbar",
            'placeholder': 'Review this game…',
      
            }))
    class Meta:
        model = Comments
        fields = ['comment', 'stars']