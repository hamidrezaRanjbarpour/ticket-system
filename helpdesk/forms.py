from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirmation = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError('User with username {} already exists.'.format(username))
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user.exists() and len(email) > 0:
            raise forms.ValidationError('A user with this email already exists.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must contain at least 8 words.')

        return password

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_pass = cleaned_data.get('password_confirmation')
        if password != confirm_pass:
            raise forms.ValidationError("Passwords don't match!")




