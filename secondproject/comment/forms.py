from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class ContactForm(forms.Form):
    name = forms.CharField(initial='Some name...', required=True)
    last_name = forms.CharField(initial='Some last name...', required=True)
    phone = forms.RegexField(regex='\(\w{3}\)\w{8}')
    birth_date = forms.DateField()
