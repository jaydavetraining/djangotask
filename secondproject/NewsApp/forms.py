from django import forms
from .models import RegistrationForm

class RegistrationFormsUser(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your username'
    }))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your password'
    }))
    email=forms.CharField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your email'
    }))
    phone=forms.CharField(max_length=100,widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your phone'
    }))

class RegistarionModelformUser(forms.ModelForm):
    class Meta:
        model=RegistrationForm
        fields=[
            'username',
            'password',
            'email',
            'phone'
        ]
        widgets ={
            'username':forms.TextInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your username'
                                    }),
            'password':forms.PasswordInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your password'
                                    }),
            'email':forms.EmailInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your email'
                                    }),
            'phone':forms.NumberInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your phone'
                                    })
        }


