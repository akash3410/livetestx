from django import forms
from .models import Post
from categories.models import Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
class SearchForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    query = forms.CharField(
        label="",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': "Enter Event's Name...", 
            'class': "form-control rounded-2 col-8"
        })
    )