from django.urls import include, path
from .views import (
    PostListCreate, 
    PostRetrieveUpdateDestroy, 
    CommentsListCreate, 
    CommentsRetrieveUpdateDestroy
)

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post_list_create'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post_RUD'),
    path('comments/', CommentsListCreate.as_view(), name='comments_list_create'),
    path('comment/<int:pk>/', CommentsRetrieveUpdateDestroy.as_view(), name='comment_RUD'),
]