from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from django.shortcuts import redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import MySQLdb


def detail(request, id_blog):
    try:
        post = Article.objects.get(id=id_blog)
        # post.content = markdown(post.content, ['codehilite'])
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'page.html', {'post': post})


def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def time_axis(request):
    post_list = Article.objects.all()
    return render(request, 'Axis.html', {'article_list': post_list})


def classify(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def my_info(request):
    return render(request, 'aboutme.html')


def search(request):
    if 's' in request.GET:
        error = False
        post_list = []
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            posts = Article.objects.filter(title__icontains=s)
        if len(posts) == 0:
            error = True
        else:
            pagintor = Paginator(posts, 12)
            page = request.GET.get('page')
            try:
                post_list = pagintor.page(page)
            except PageNotAnInteger:
                post_list = pagintor.page(1)
            except EmptyPage:
                post_list = pagintor.page(pagintor.num_pages)
        return render(request, 'result.html', {'post_list': post_list, 'error': error, 's': s})
    return redirect('/')

