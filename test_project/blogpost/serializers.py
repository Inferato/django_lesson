from rest_framework import serializers
from .models import Comments, Posts

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'post', 'content', 'created_at']

class PostsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Posts
        fields = ['id', 'title', 'content', 'created_at', 'comments']


class CommentManualSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=255)

class PostCommentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=255)
    comments = CommentManualSerializer(many=True)

    def create(self, validated_data):
        post = Posts(title=validated_data['title'], content=validated_data['content'])
        post.save()
        for comment in validated_data['comments']:
            new_comment = Comments(post=post, content=comment['content'])
            new_comment.save()
        return post


