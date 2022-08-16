from django import forms
from .models import Post
from .widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        
    image = forms.ImageField(label='BlogImage', required=False, widget=CustomClearableFileInput)