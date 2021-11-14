from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_posts(request):
    # Get a list of the nth most recent posts from the database
    # Build the basic structure of the page
    # In the main tag, include those posts formatted
    pass

def create_post(request):
    # Receive the data to create a post from a form
    # Build it through a Model
    # Put it inside the database
    pass

def update_post(request):
    # Get a post ID
    # Take the post from the database
    # Update it according to the request
    # Put it back in
    pass
