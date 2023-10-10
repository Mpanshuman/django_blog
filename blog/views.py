from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
# Create your views here.

class PostDetailView(DetailView):
    model = Post
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context)


def about(request):
    return render(request, "blog/about.html")
