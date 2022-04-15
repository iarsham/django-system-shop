from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Your Password',
            'class': 'form-control'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Your Confirm Password',
            'class': 'form-control'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'age',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter Your First Name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Your Last Name'
            self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email Address'
            self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Your Phone Number'
            self.fields['age'].widget.attrs['placeholder'] = 'Enter Your Age'
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        info = super(RegisterForm, self).clean()
        password = info.get('password')
        confirm_password = info.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password is Not Same !")
        return info
