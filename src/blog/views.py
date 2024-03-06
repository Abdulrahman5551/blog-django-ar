from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import NewComment

# Create your views here.

def home(request):
    posts = Post.objects.all()
    comment = Comment.objects.all()
    context = {
        'title': "الصفحه الرئيسية",
        'posts': posts,
        'comments': comment,
    }
    return render(request, 'blog/index.html', context)

def about(request):
    posts = Post.objects.all()
    context = {
        'title': 'من أنا',
        'posts': posts
    }
    return render(request, 'blog/about.html', context)

def post_detail(request, post_id):
    comment_form = NewComment()
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk=post_id)
    comment = post.comments.filter(active=True) ###########
    context = {
        'title': post.title,
        'post': post,
        'posts': posts,
        'comments': comment,
        'comment_form': comment_form
    }

    if request.method == 'POST':
        comment_form = NewComment(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    return render(request, 'blog/detail.html', context)
