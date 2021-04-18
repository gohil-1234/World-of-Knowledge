from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.


posts = [
    {
        'name': 'Gohil',
        'title': 'first post',
        'content': 'first post of blog',
        'date': '10 october 2020'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    paginate_by = 5
    return render(request, 'note/index.html', context)


def detail(request, id):
    detail_post = {
        'posts': Post.objects.get(id=id)
    }

    return render(request, 'note/post-details.html', detail_post)


def upload(request):
    if request.method == 'GET':
        return render(request, 'note/upload.html')
    else:
        name = request.POST.get('name')
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date')

        post = Post.objects.create(
            name=name, title=title, content=content, date=date)
        post.save()
        return HttpResponse('<h1>Uploaded Successfully</h1>')


def delete(request, id):

    delete_post = Post.objects.get(id=id)

    delete_post.delete()

    return HttpResponse('<h1>Delete Successfully</h1>')
