from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,EmployeeBasicDetails,EducationDetail,WorkExperience,LanguageMaster,ReferenceContact,preferences,TechnologyMaster
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
	# cpassword=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your confirm password'}),label='Confirm Password')
	def clean_username_check(self):
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		print(username,"<><><<>")
		if username=="jat" or username==None:
			print("*********")
			raise ValidationError("enter Username name")
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Email already exists")
		return email
	
	def clean_cpassword(self):
		cleaned_data = super().clean()
		p = cleaned_data.get('password')
		cp = cleaned_data.get('cpassword')
		if p != cp:
			raise forms.ValidationError('Password And Confirm Password Do Not Match')
		return cp

	
    



	class Meta:
		model = User
		fields = ['username','password1','password2','email','phone','first_name','last_name']
		widgets ={
            'username':forms.TextInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your username'
                                    }),
            'email':forms.EmailInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your email'

                                    }),
			'password1':forms.PasswordInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your password'
                                    }),
			'password2':forms.PasswordInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your password'
                                    }),
			'first_name':forms.TextInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your firstname'
                                    }),
			'last_name':forms.TextInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your lastname'
                                    }),
            'phone':forms.NumberInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your phone'
                                    }),
        }

class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
            
        )
    )
	
class EmployeeBasicDetailsForms(forms.ModelForm):

    class Meta:
        CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ]
        RELATIONSHIP_CHOICES = [
        ('single', 'single'),
        ('married', 'married'),
        ]
        model=EmployeeBasicDetails
        fields='__all__'
	
        widgets={    
			'first_name':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your name'
            }),
			'last_name':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Enter ypur surname'
            }),
			'designation':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Enter ypur designation'
            }),
			'phone':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Enter ypur phone number'
            }),
			'gender':forms.RadioSelect(choices=CHOICES),
			'email':forms.EmailInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'Enter your email'

                                    }),
			'relationship_status':forms.RadioSelect(choices=RELATIONSHIP_CHOICES),
			'address1':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Enter your address'
            }),
			'address2':forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Enter your address2'
            }),
			'city':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your surname'
            }),
			'state':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your state'
            }),
			'zipcode':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your area zipcode'
            }),
			'birthday':forms.DateInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your state'
            })
		
        }
      
class EducationDetailForms(forms.ModelForm):


	class Meta:
		model=EducationDetail
		fields='__all__'
		widgets={
			'university':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your university'
            }),
			'passingyear':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your passingyear'
            }),
			'percentage':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your percentge'
            })
			
        }

class WorkExperienceForms(forms.ModelForm):
	class Meta:
		model=WorkExperience
		fields='__all__'
		widgets={
			'compname':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your company name'
            }),
			'designation':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your designation'
            }),
			'durationfrom':forms.DateInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your from'
            }),
			'durationto':forms.DateInput(attrs={
				'class':'form-control',
				'placeholder':'Enter your to'
            })
        }

class LanguageMasterForms(forms.ModelForm):
	class Meta:
		model=LanguageMaster
		fields='__all__'


class ReferenceContactForms(forms.ModelForm):
	class Meta:
		model=ReferenceContact
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Enter reference person name'
		}),
		'phone':forms.NumberInput(attrs={
				'class':'form-control',
				'placeholder':'Enter ypur phone number'
            }),
		'relation':forms.TextInput(attrs={
			'class':'form-control',
		}),
		}

class preferencesForms(forms.ModelForm):
	class Meta:
		model=preferences
		fields='__all__'
		widgets={
		'preferencelocation':forms.SelectMultiple(),
		'noticeperiod':forms.NumberInput(attrs={
			'class':'form-control',
			'placeholder':'enter number',
			'style':"width:156px"
		}),
    				
		'expectedctc':forms.NumberInput(attrs={
			'class':'form-control',
			'placeholder':'enter number',
			'style':"width:156px"
		}),
		'currentctc':forms.NumberInput(attrs={
			'class':'form-control',
			'placeholder':'enter number',
			'style':"width:156px"
		})
		}
		
class TechnologyMasterForms(forms.ModelForm):
	class Meta:
		model=TechnologyMaster
		fields='__all__'
		widgets={
			'techvalue':forms.CheckboxInput(),
			'techproficiency':forms.RadioSelect()
		}