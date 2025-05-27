from django import forms
from .models import Post

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=10)
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']



