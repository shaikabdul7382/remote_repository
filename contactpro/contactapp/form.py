from django import forms
from .models import ContactData
class Contactform(forms.Form):
    first_name=forms.CharField(
        label="enter your first name",
        widget=forms.TextInput(
            attrs={
                'class':'form.control',
                'placeholder':'first_name'
            }
        )

    )
    last_name=forms.CharField(
        label="enter your last name",
        widget=forms.CharField(
            attrs={
                'class':'form.control',
                'placeholder':'last_name'
            }
        )
    )
    salary=forms.IntegerField(
        label="enter your salary",
        Widget=forms.IntegerField(
            attrs={
                'class':'form.control',
                'placeholder':'salary'

            }
        )



    )
    location=forms.CharField(
        label="enter your location",
        widget=forms.CharField(
            attrs={
                'class':'form.control',
                'placeholder':'loc'
            }
        )
    )
    mobile=forms.IntegerField(
        label="enter your mobile number",
        widget=forms.IntegerField(
            attrs={
                'class':'form.control',
                'placeholder':'mobile'
            }
        )

    )