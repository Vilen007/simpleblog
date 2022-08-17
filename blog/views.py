from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import post,blogs_comment
from blog.templatetags import initialize

# Create your views here.

# @login_required
def blogHome(request):
    posts = post.objects.all()
    return render(request, "blog/blogHome.html",{'posts': posts})

def blogPost(request,slug):
    Post = post.objects.filter(slug=slug).first()
    Post.views = Post.views + 1
    Post.save()
    comment = blogs_comment.objects.filter(posts=Post,parent = None).order_by("-sno")
    replies = blogs_comment.objects.filter(posts = Post).exclude(parent=None)
    reply = {}
    for i in replies:
        if i.parent.sno not in reply.keys():
            reply[i.parent.sno] = [i]
        else:
            reply[i.parent.sno].append(i)
    return render(request, "blog/blogPost.html", {'Post': Post, 'comment':comment, 'user': request.user, 'reply':reply})

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        Post= post.objects.get(sno=postSno)
        commentSno = request.POST.get('commentSno')
        if commentSno == "":
            comment=blogs_comment(comment= comment, user=user, posts=Post)
            comment.save()
        else:
            parent = blogs_comment.objects.get(sno=commentSno)
            comment=blogs_comment(comment= comment, user=user, posts=Post, parent=parent)
            comment.save()
    return redirect(f"/blog/{Post.slug}")
    