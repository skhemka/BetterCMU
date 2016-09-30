from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.order_by('posted_on')
    context = { 'posts': posts }
    return render(request, 'posts/index.html', context)

def post(request,id):
    post = get_object_or_404(Post,id)
    context = { 'post': post }
    return render(request, 'posts/detail.html', context)
    
