from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            name=self.cleaned_data['name'],
            is_active=True,
        )
        return user


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()