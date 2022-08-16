from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

def blogpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/blogpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def add_post(request, slug):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New post added!')
            return redirect(reverse('add_post'))
        else:
            messages.error(request, 'Something went wrong! The post was not added.')
    else:
        form = PostForm()
        
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
