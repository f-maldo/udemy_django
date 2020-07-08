from rest_framework import serializers
from .models import Category, Type, Element
from comment.models import Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ElementSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)

    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Element
        fields = '__all__'

    def get_comment_count(self, obj):
        return obj.comments.count()
