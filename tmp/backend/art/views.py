from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Art
from .serializers import ArtSerializer

##########################################################################67

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_art(request):
    art = Art.objects.all()
    serializer = ArtSerializer(art, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_art(request):
    if request.method == 'GET':
        art = Art.objects.filter(user_id=request.user.id)
        serializer = ArtSerializer(art, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        data = request.data
        serializer = ArtSerializer(data=data)
        if serializer.is_valid(data):
            art = Art.objects.get(data.id)
            art.artist = data.artist
            art.artwork_date = data.artwork_date
            art.artwork_group = data.artwork_group
            art.artwork_collection = data.artwork_collection
            art.artwork_name = data.artwork_name
            art.artwork_description = data.artwork_description
            art.price = data.price
            art.quantity = data.quantity
            art.in_stock = data.in_stock
            art.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        art = Art.objects.get(id=request.data.id)
        art.delete()
        return Response('Item deleted')
##########################################################################67
