from django.shortcuts import render

from .models import Post

def blogpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/blogpage.html', {'posts': posts})
