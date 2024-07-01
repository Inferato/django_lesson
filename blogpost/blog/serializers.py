from rest_framework import serializers
from .models import Posts
from comments.serializers import CommentsSerializer

class PostsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Posts
        fields = ['id', 'title', 'content', 'created_at', 'comments']
