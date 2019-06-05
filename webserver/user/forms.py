from django import forms

from .models import User
from trade.models import RegionTable

class UserForm(forms.ModelForm):
    # 서명을 담을 필드.
    sigData = forms.CharField(max_length = 132, widget = forms.HiddenInput(attrs = {
        'id': 'sigData'
    }))

    class Meta:
        model = User
        fields = ('user_name', 'user_contact', 'user_region')
        labels = {
            'user_name': '이름',
            'user_contact': '전화번호',
            'user_region': '거주지'
        }
        widgets = {
            'user_name': forms.TextInput(attrs = {
                'class': 'w3-input w3-border'
            }),
            'user_contact': forms.TextInput(attrs = {
                'class': 'w3-input w3-border'
            })
        }
