from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.safestring import mark_safe

class InfosForm(forms.Form):

    orga_name = forms.CharField(max_length=100, label="Organization name")

    def clean(self):

        cleaned_data = super(InfosForm, self).clean()
        orga_name = cleaned_data.get('orga_name')

        if not orga_name:

            raise forms.ValidationError(

                "Organisation non trouvée."

                )


        return cleaned_data

class AuthenticationFormWithRequiredField(AuthenticationForm):
    required_checkbox = forms.BooleanField(required=True, label=mark_safe('I accept cookies and the site\'s chart '))
