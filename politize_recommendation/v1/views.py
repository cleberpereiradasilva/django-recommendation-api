from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post, Tag, PostView, User as Visitor
from .serializers import PostSerializer, TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):        
        #TODO insert filter to post visited and suggested
        print('Passando novamente...')
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):        
        visitor = Visitor()
        visitor.post_id = pk
        visitor.user_id = request.user.id
        visitor.save()
        queryset = Post.objects.get(pk=pk)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)



class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


