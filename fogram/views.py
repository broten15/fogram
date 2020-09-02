from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    """A landing page for the fogram"""
    return render(request, 'fogram/landing.html')