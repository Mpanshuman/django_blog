from django.shortcuts import render

# Create your views here.
BLOGS = [
    {
        "author": "CoreyMS",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28, 2018",
    },
]


def index(request):
    context = {"posts": BLOGS}
    return render(request, "blog/index.html", context)


def about(request):
    return render(request, "blog/about.html")
