from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

def home(request):
    """The main page of the web app"""
    posts = Post.objects.order_by('-date_added')
    return render(request, 'feed/feed_view.html', {'posts':posts})

@login_required(login_url="login")
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save post to DB
            return redirect('home')
    else: 
        form = forms.CreatePost()
    return render(request, 'feed/create_post.html', {'form':form}) 
