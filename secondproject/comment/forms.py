from django import forms
from .models import Comment, TypeContact
from django.core.validators import MaxLengthValidator, EmailValidator


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class ContactForm(forms.Form):
    CHOICE = (
        (1, 'Business'),
        (2, 'Greetings'),
        (1, 'Others')
    )

    name = forms.CharField(validators=[MaxLengthValidator(20)])
    last_name = forms.CharField(required=False)
    phone = forms.RegexField(regex='\(\w{3}\)\w{8}')
    birth_date = forms.DateField()
    email = forms.EmailField()
    # image = forms.ImageField(required=False)
    # type_contact = forms.ChoiceField(choices=CHOICE, initial=2)
    type_contact = forms.ModelChoiceField(queryset=TypeContact.objects.all(), initial=1)
    document = forms.FileField(required=False)
    terms = forms.BooleanField()
