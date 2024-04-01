from .models import Bonedata
from django.forms import ModelForm, TextInput

class BonedataForm(ModelForm):
    class Meta:
        model = Bonedata
        fields = ['first_author','title', 'year_pub']

        widgets ={
            "first_author": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Первый автор',
            }),
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название статьи',
            }),
            "year_pub": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Год публикации',})
        }