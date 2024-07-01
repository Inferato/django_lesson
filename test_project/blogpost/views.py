from rest_framework import generics
from django.views.generic.list import ListView
from .models import Posts, Comments
from .serializers import PostsSerializer, CommentsSerializer, PostCommentSerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostCommentSerializer

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class CommentsListCreate(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class CommentsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class PostsList(ListView):
    template_name = 'post_list.html'
    model = Posts
    context_object_name = 'posts'
