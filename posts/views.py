from django.shortcuts import render, redirect
from django.http import HttpResponse

# Models
from posts.models import BlogPost

# Create your views here.

def show_posts(request):
    # Get a list of the nth most recent posts from the database
    # Build the basic structure of the page
    # In the main tag, include those posts formatted

#    posts = [ 
#            {'title': 'titulo', 'description': 'descripcion', 'author': 'autor', 'id': '1'},
#            {'title': 'titulo2', 'description': 'descripcion2', 'author': 'autor2', 'id': '2'}
#    ]
    blogposts = BlogPost.objects.all()

    return render(request, 'posts/posts.html', {'posts': blogposts})

def create_post(request):
    # Receive the data to create a post from a form
    # Build it through a Model
    # Put it inside the database
    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        description = request.POST.dict()["description"]
        if str(request.user) == 'AnonymousUser':
            author_id = None
        else:
            author_id = request.user
        blogpost = BlogPost(title=title, description=description, content=content, author_id=author_id)
        blogpost.save()
        post_id = blogpost.pk

        return redirect('posts/{}'.format(post_id))
    return render(request, 'posts/create_post.html')


def update_post(request):
    # Get a post ID
    # Take the post from the database
    # Update it according to the request
    # Put it back in
    pass
