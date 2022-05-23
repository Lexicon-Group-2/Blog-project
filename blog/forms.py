from xml.etree.ElementTree import Comment
from django import forms
from django.contrib.auth.models import User
from blog.models import UserProfileInfo, Comment

class UserForm(forms.Form, forms.ModelForm):
  password   = forms.CharField(widget=forms.PasswordInput())
  
  class Meta():
    model = User
    fields = ['username', 'email', 'password']
    
class UserProfileInfoForm(forms.ModelForm):
  class Meta():
    model = UserProfileInfo
    fields = ['portfolio_site', 'profile_pic']

class CommentForm(forms.ModelForm):
  class Meta():
    model = Comment
    fields = ['name', 'email', 'body']
