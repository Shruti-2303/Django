from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")
class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher'] {{{{ we will not use much this type of a code }}}}
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT !")
    #     return botcatcher

    def clean(self):
        all_data_clean = super().clean()
        email = all_data_clean['email']
        vmail = all_data_clean['verify_email']

        if email!=vmail:
            raise forms.ValidationError("EMAILS SHOULD MATCH")

