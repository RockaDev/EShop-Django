from users.models import ThisUser
from django import forms

class AdminForm(forms.ModelForm):
    email = forms.EmailField(error_messages=
        {
            'invalid': 'Please provide a valid email address.'
        },
        required=True,
            widget=forms.EmailInput(
                attrs=
                {
                    'class': 'form',
                    'placeholder': 'Email'
                }
            ))
    password = forms.CharField(label='Password',widget= forms.PasswordInput(attrs=
    {
        'placeholder': 'Password'
    }))

    class Meta:
        model = ThisUser
        fields = ("email","password")






