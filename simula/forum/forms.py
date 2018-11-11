from django import forms
from .models import *

class PostForm(forms.ModelForm):
    image = forms.FileField(required=False)
    class Meta:
      model = Post
      fields = [
        'body',
        'image',
        'category',
    ]
    fields_required = ['body', 'image', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # exclude = ['author', 'updated', 'created', ]
        fields = ['body']
        widgets = {
            'body': forms.TextInput(
                attrs={'id': 'comment-text', 'required': False, 'placeholder': 'Répondre'}
            ),
}