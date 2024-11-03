# forms.py
from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','image', 'body','name','description']

  
