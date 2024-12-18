from django import forms
from .models import Review
from django_ckeditor_5.widgets import CKEditor5Widget
        
class PostForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'category', 'image')
        widgets = {
            "content": CKEditor5Widget(config_name="extends")
        }