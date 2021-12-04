from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from posts.comments.models import Comment
from posts.models import BlogPost
# Create your views here
@login_required(login_url='login')
def create_comment(request, post_id):
   # Ctrl + W; Ctrl + F
    # posts/views.py
    if request.method == 'POST':
        content = request.POST["content"]
        author = request.user
        blogpost=None
        try:
            blogpost = BlogPost.objects.get(pk=post_id)
        except:
            HttpResponse("SEXO")
        Comment.objects.create(author=author, post=blogpost, content=content, parent_comment=None)

    return redirect('posts', post_id=post_id)
        

def delete_comment(request, comment_id):
    pass
