from multiprocessing import context
from django.shortcuts import redirect, render

from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.all()
    context = {
        'object_list': qs
    }
    return render(request, "blogapp/post_list.html", context)

def post_create(request):
    # form = PostForm(request.POST or None, request.POST or None)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blogapp:list")
    context = {
        'form': form
    }
    return render(request, 'blogapp/post_create.html', context)

