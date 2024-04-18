from django import forms
from .models import *
class MyForm(forms.ModelForm):
    class Meta:
        model=Client
        
        
        fields="__all__"
        widget={'Username':forms.TextInput(attrs={'style':'width:250px;height:25px;'}),
                 'Password':forms.TextInput(attrs={'style':'width:250px;height:25px;'})}
            
       