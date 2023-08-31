from django import forms
from .models import blogs


class create_update_post(forms.ModelForm):
    class Meta:
        model = blogs
        fields = ['title', 'text', 'author', 'status']

