from re import template
from django.shortcuts import render

def Profile(request):
    """Display user profile"""
    template = 'profiles/profile.html'
    context = {}
    
    return render(request, template, context)