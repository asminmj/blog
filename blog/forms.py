from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostUpdateForm(UserCreationForm):
    title = forms.CharField(label="",  widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    content = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Content'}))
   


    class Meta:
        model = Post
        fields = ['title', 'content',]