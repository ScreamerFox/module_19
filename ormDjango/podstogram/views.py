from django.shortcuts import render
from .models import *
import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def news_list(request):
    if 'posts_per_page' in request.GET:
        request.session['posts_per_page'] = request.GET['posts_per_page']
    posts_per_page = request.GET.get('posts_per_page', 5)
    news = News.objects.all().order_by('-created_at')
    random_news = random.choice(news)
    paginator = Paginator(news, int(posts_per_page))
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'news': news,
        'random_news': random_news,
        'page_range': paginator.page_range,
        'current_page': page_number,
        'page_obj': page_obj,
        'posts_per_page': posts_per_page,
    }
    return render(request, 'main.html', context)
