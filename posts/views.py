from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests


# POSTS VIEW
def posts(request):
    post_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(post_url)
    data = response.json()

    page = request.GET.get('page', 1)

    paginator = Paginator(data, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog-listing.html', {
        'postdata': posts
    })


# POST DETAILS VIEW
def post_details(request, post_id):
    post_details_url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    comments_url = f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments'
    response1 = requests.get(post_details_url)
    response2 = requests.get(comments_url)
    post_details = response1.json()
    comments = response2.json()

    return render(request, 'blog-post.html', {
        'post_details': post_details,
        'comments': comments
    })
