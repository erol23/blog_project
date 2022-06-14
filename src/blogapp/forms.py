from dataclasses import field
from pyexpat import model
from django import forms
from .models import Category, Post, Comment

class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select Category')
    class Meta:
        model = Post
        field = (
            'title',
            'content',
            'image',
            'category',
            'status',            
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        field('content',)