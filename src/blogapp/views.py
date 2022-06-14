from multiprocessing import context
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    context = {
        'object_list': qs
    }
    return render(request, "blogapp/post_list.html", context)
