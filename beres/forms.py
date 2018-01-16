from django.forms import ModelForm
from .models import Topic
from django.views.generic.edit import CreateView
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
                
class CustomUserCreationForm(forms.Form):
    username  = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email     = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
        
        
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        existing_users_with_name = User.objects.filter(username=username)
        if existing_users_with_name.count():
            raise ValidationError('Username already exists')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        existing_users_with_email = User.objects.filter(email=email)
        if existing_users_with_email.count():
            raise ValidationError("Email already exists")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']      
        )
        return user
        