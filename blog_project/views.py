from django.shortcuts import render
from posts.models import Post
from posts.forms import SearchForm

def home(request):
    data = Post.objects.all()
    forms = SearchForm()
    if request.method == "POST":
        forms = SearchForm(request.POST)
        if forms.is_valid():
            category = forms.cleaned_data.get('category')
            query = forms.cleaned_data.get('query')
            
            if query:
                data = data.filter(title__icontains=query)
            if category:
                data = data.filter(category=category)
   
    return render(request, 'home.html', {'data': data, 'forms': forms})