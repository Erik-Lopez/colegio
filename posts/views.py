from django.shortcuts import render, redirect
from django.http import HttpResponse

# Python
from functools import reduce
import subprocess

# Models
from posts.models import BlogPost
from categories.models import Category
# Decorators
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, authenticated_user, allowed_groups
# Create your views here.

def hex_sum(a, b):
    """a y b vienen en formato '#abcdef', son sumadas y se sacan en mismo formato"""
    dec_result = int(a[1:], 16) + int(b[1:], 16)
    hex_result = hex(dec_result)

    if int(hex_result[2:], 16) > 0xFFFFFF:
        hex_result = 0xFFFFFF

    hex_result = "#" + hex_result[2:]
    return hex_result

def show_posts(request, post_id=0):
    # Get a list of the nth most recent posts from the database
    # Build the basic structure of the page
    # In the main tag, include those posts formatted
    user = None

    if post_id == 0:
        blogposts = BlogPost.objects.order_by('-posted_at')
        categories = [blogpost.category_set.all() for blogpost in blogposts]
        colors = []

        for blogpost in blogposts:
            local_colors = []
            if blogpost.category_set.exists():
                for category in blogpost.category_set.all():
                    local_colors.append(category.color)
            else:
                local_colors.append("#241d17")
            colors.append(local_colors)

        true_colors = []
        for color_list in colors:
            if type(color_list) == str:
                true_colors.append(color_list)
            elif type(color_list) == list and color_list:
                true_colors.append(reduce(lambda a,b: hex_sum(a,b), color_list))
            else:
                true_colors.append("#000000")

        posts_and_colors = zip(blogposts, true_colors)
        return render(request, 'posts/posts.html', {'posts': blogposts, 'allowed_groups': ['admin', 'super_admin'], 'posts_and_colors': posts_and_colors})

    try:
        blogpost = BlogPost.objects.get(pk=post_id)
        comments = None
        if blogpost.comment_set.exists():
            comments = blogpost.comment_set.all()

        html_content = subprocess.check_output(["./scripts/pandoc.sh", blogpost.content]).decode('utf-8')
        return render(request, 'posts/post.html', {'blogpost': blogpost, 'content': html_content, 'comments': comments, 'post_id': post_id})
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

        blogpost = BlogPost.objects.create(title=title, thumbnail=thumbnail, description=description, content=content, author_id=author_id)

        for key in request.POST.keys():
            if not key.startswith("category_"):
                continue
            category = Category.objects.get(pk=key[9:])
            blogpost.category_set.add(category)
        blogpost.save()

        post_id = blogpost.pk

        return redirect('posts', post_id=post_id)
    categories = Category.objects.all()
    
    user_clubs = None
    if request.user.is_authenticated and (request.user.profile.clubs.exists() or request.user.club_set.exists()):
        user_clubs = request.user.profile.clubs.all()
        user_clubs = user_clubs|request.user.club_set.all()
    return render(request, 'posts/create_post.html', {'categories': categories, 'user_clubs': user_clubs})

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
    if request.user.is_staff:
        permission = True
    if blogpost.author_id:
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
