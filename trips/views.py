from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
# Create your views here.

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
        'fullname': 'chenghaolee',
    })



def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})