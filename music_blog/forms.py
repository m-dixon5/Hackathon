from django import forms
from .models import Review, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'category', 'image', 'location')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
