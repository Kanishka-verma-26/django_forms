from django import forms
from django.core import validators

# creating own custom validator
def chk_for_z(val):
    if val[0].lower() != 'z':
        raise forms.ValidationError("Name should start with 'z'")

class survey_form(forms.Form):
    name = forms.CharField(validators=[chk_for_z])
    email = forms.EmailField()
    confirm_email = forms.EmailField(label = 'Confirm Email')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_wipe = super().clean()
        print('all_wipe',all_wipe)
        email = all_wipe['email']
        vmail = all_wipe['confirm_email']

        if email!=vmail:
            raise forms.ValidationError("make sure emails match")



    # # django built-in validator
    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])



    # validation using clean_ function

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Gotcha Bot!")
    #     return botcatcher