from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import list_route

from .models import Post, Tag, PostView
from .serializers import PostSerializer, TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @list_route(methods=['get'])
    def news(self, request):        
        visitedPosts = PostView.objects.filter(user_id = request.user.id)
        visitedIds = [visited.post_id for visited in visitedPosts]
        visitedTagsPosts = [post.post.tags.all() for post in visitedPosts]     

        visitedTagIds = []
        for visitedTag in visitedTagsPosts:        
            visitedTagIds += [tag.id for tag in visitedTag]

        queryset = Post.objects.all().exclude(pk__in=visitedIds).filter(tags__id__in=visitedTagIds)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


   

    def retrieve(self, request, pk=None):

        post = Post.objects.get(pk=pk)        
        postView = PostView()
        postView.post = post
        postView.user = request.user
        postView.save()        

        serializer = PostSerializer(post)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


