from django import forms

from .models import Dog, Picture

class DogForm(forms.ModelForm):

    class Meta:
        model = Dog
        fields = ('dog_name', 'dog_coat_length', )