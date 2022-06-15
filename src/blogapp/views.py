from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post
from .forms import PostForm

def post_list(request):
    qs = Post.objects.filter(status="p")
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

def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    context= {
        "object": obj
    }
    return render(request, "blogapp/post_detail.html", context)

def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("blogapp:list")
    context = {
        "object": obj,
        "form": form
    }
    return render(request, "blogapp/post_update.html", context)