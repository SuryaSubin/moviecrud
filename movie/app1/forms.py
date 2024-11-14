#Form definition
from django import forms
from app1.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie #model name
        fields='__all__'   #all fields inside the model