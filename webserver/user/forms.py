from django import forms

from .models import User

class UserForm(forms.ModelForm):
    sigData = forms.CharField(max_length = 132, widget = forms.HiddenInput(attrs = {
        'id': 'sigData'
    }))

    class Meta:
        model = User
        fields = ('user_name', 'user_contact', 'user_region')
