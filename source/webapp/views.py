from django.shortcuts import render, redirect

from .models import Comment


def index_view(request):
    comments = Comment.objects.filter(status='active')
    context = {
        'comments': comments
    }
    return render(request, "index.html",context)

def delete(request):
    context = {
    }
    return render(request, "index.html",context)

def create(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        c = Comment(
            author=request.POST.get('author'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        c.save()
        return redirect('index_view')


def update(request):
    context = {
    }
    return render(request, "index.html",context)