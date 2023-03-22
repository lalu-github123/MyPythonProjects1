from django import forms
from .models import TodoModel

class Update_Form(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['name','priority','date']