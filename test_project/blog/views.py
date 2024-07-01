import requests
from urllib.parse import urljoin
from django.shortcuts import render
from django.conf import settings

def post_detail(request, post_id):
    post_url = urljoin(settings.BLOG_BASE_URL, f'/api/post/{post_id}')
    response = requests.get(post_url)
    post = response.json()
    return render(request, 'post_detail.html', {'post': post})
