from .models import Good
from django import forms

class AddForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ('name','description','quantity')

