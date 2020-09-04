from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    """The main page of the web app"""
    posts = Post.objects.order_by('-date_added')
    return render(request, 'feed/feed_view.html', {'posts':posts})