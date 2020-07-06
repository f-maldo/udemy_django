from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        """widgets = {
            'text': TextInput(attrs={
                'class': 'form-input'
            })
        }
        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            super.fields['text'].widgets.attrs.update({'class': 'form-input'})"""
