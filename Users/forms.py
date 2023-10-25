from django import forms
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

class RegistrationForm(UserCreationForm):
    """
      Form for Registering new users 
    """
    email = forms.EmailField(max_length=60, help_text = None)
    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2')
      

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(RegistrationForm, self).__init__(*args, **kwargs)
      
        for fieldname in ['email','name', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control '})
            
        # for field in (self.fields['email'],self.fields['name'],self.fields['password1'],self.fields['password2']):
        #     field.widget.attrs.update({'class': 'form-control '})


class UserAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    password  = forms.CharField(label= 'Password', widget=forms.PasswordInput)

    class Meta:
        model  =  User
        fields =  ('email', 'password')
        widgets = {
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.TextInput(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')