from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'context']
        # Add Tailwind CSS classes to the form widgets
        widgets = {
            'topic': forms.TextInput(attrs={
                'class': 'w-full p-3 bg-white/70 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Post Title'
            }),
            'context': forms.Textarea(attrs={
                'class': 'w-full p-3 bg-white/70 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Write your blog post here...',
                'rows': 5
            }),
        }