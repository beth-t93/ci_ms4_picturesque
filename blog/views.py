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
def add_post(request):
    """ create a post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'New post added!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Something went wrong! The post was not added.')
    else:
        form = PostForm()
        
    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_post(request, slug):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.save()
            messages.success(request, 'Successfully updated the post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request,
                           ('Failed to update the post. '
                            'Please ensure the form is valid.'))
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)
    
@login_required
def delete_post(request, slug):
    """ Delete a post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
