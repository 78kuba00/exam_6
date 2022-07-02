from django.shortcuts import render, redirect

from .models import Comment


def index_view(request):
    comments = Comment.objects.order_by('-created_at').filter(status='active')
    context = {
        'comments': comments
    }
    return render(request, "index.html", context)


def delete(request, id):
    Comment.objects.filter(id=id).delete()
    return redirect('index_view')


def create(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        author = request.POST.get('author')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if len(author) < 2:
            return render(request, "create.html",
                          {'result': 'error', 'message': 'author minimum 2 characters required'})

        if len(message) > 255:
            return render(request, "create.html",
                          {'result': 'error', 'message': 'message maximum 255 characters required'})

        c = Comment(
            author=author,
            email=email,
            message=message,
        )
        c.save()
        return redirect('index_view')


def update(request, id):
    if request.method == "GET":
        comment = Comment.objects.filter(id=id).first()
        context = {
            'id': id,
            'author': comment.author,
            'email': comment.email,
            'message': comment.message,
        }
        return render(request, "update.html", context)
    else:
        author = request.POST.get('author')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if len(author) < 2:
            return render(request, "create.html",
                          {'result': 'error', 'message': 'author minimum 2 characters required'})

        if len(message) > 255:
            return render(request, "create.html",
                          {'result': 'error', 'message': 'message maximum 255 characters required'})


        Comment.objects.filter(id=id).update(
            author=author,
            email=email,
            message=message,
        )
        return redirect('index_view')
