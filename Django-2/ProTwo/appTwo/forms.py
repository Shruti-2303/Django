from django import forms
from appTwo.models import User

class NewForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'