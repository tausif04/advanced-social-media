from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image')
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'What is on your mind?',
            }),
        }

    def clean(self):
        cleaned = super().clean()
        content = cleaned.get('content', '').strip()
        image = cleaned.get('image')
        if not content and not image:
            raise forms.ValidationError('Add some text or an image before publishing.')
        return cleaned
