from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'Handla',
        'title': 'Blog Post 1',
        'content': 'My First Post',
        'date_posted': 'January 25th, 2024'
    },
    {
        'author': 'Stacy',
        'title': 'Blog Post 2',
        'content': 'My Second Post',
        'date_posted': 'January 25th, 2024'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})