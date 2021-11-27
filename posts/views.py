from django.shortcuts import render, redirect
from django.http import HttpResponse

# Models
from posts.models import BlogPost
# Decorators
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, authenticated_user, allowed_groups
# Create your views here.

def show_posts(request, post_id=0):
    # Get a list of the nth most recent posts from the database
    # Build the basic structure of the page
    # In the main tag, include those posts formatted
    user = None
#    if request.user.is_authenticated and request.user.groups.exists():
#        user = {
#            "user_id": request.user.pk,
#            "groups": request.user.groups.all()[0].name
#        }

    if post_id == 0:
        blogposts = BlogPost.objects.order_by('-posted_at')
        return render(request, 'posts/posts.html', {'posts': blogposts, 'allowed_groups': ['admin', 'super_admin']})
    try:
        blogpost = BlogPost.objects.get(pk=post_id)
        return render(request, 'posts/post.html', {'blogpost': blogpost})
    except:
        return HttpResponse("El post no existe")

def create_post(request):
    # Receive the data to create a post from a form
    # Build it through a Model
    # Put it inside the database
    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        description = request.POST.dict()["description"]

        if "thumbnail" in request.FILES:
            thumbnail = request.FILES["thumbnail"]
        else:
            thumbnail = None

        if str(request.user) == 'AnonymousUser':
            author_id = None
        else:
            author_id = request.user

        blogpost = BlogPost(title=title, thumbnail=thumbnail, description=description, content=content, author_id=author_id)
        blogpost.save()
        post_id = blogpost.pk

        return redirect('posts', post_id=post_id)
    return render(request, 'posts/create_post.html')

@login_required(login_url='login')
#@allowed_groups(allowed_roles=['admin', 'super_admin'])
def delete_post(request, post_id):    
    try:
        blogpost = BlogPost.objects.get(pk=post_id) 
    except:
        return HttpResponse("El post no existe") 
    permission = False
    group = None

    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        if group in ['admin', 'super_admin']:
            permission = True

    if blogpost.author_id.pk == request.user.pk:
        permission = True
        
    if permission:
        blogpost.delete()
        return redirect('posts')
    else:
        HttpResponse("No tienes permiso, puto")

def update_post(request):
    # Get a post ID
    # Take the post from the database
    # Update it according to the request
    # Put it back in
    pass
