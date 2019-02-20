from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Tag

# Serializers define the API representation.
class PostSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Post
        fields = ('id', 'name', 'tags' )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

