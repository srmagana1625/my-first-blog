from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('city_state', 'dive_site', 'difficulty_level', 'description')
