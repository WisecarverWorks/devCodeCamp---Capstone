from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Post
from .serializers import PostSerializer

############################################################################

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, AllowAny])
def all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid(data):
            posts = Post.objects.get(data.id)
            posts.user = data.user
            posts.title = data.title
            posts.text = data.text
            posts.post_image = data.post_image
            posts.website = data.website
            posts.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post = Post.objects.get(id=request.data.id)
        post.delete()
        return Response('Item deleted')
############################################################################
