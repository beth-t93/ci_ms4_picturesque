from django.shortcuts import render

from django.shortcuts import render

def blog(request):
    return render(request, 'blog/blog.html')