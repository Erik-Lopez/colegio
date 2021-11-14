from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_posts(request):
    # Get a list of the nth most recent posts from the database
    # Build the basic structure of the page
    # In the main tag, include those posts formatted

    posts = [ 
            {'title': 'titulo', 'description': 'descripcion', 'author': 'autor', 'id': '1'},
            {'title': 'titulo2', 'description': 'descripcion2', 'author': 'autor2', 'id': '2'}
    ]
    return render(request, 'posts/posts.html', {'posts': posts})

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
