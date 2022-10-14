from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Bulletin
from .serializers import BulletinSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_bulletin(request):
    bulletin = Bulletin.objects.all()
    serializer = BulletinSerializer(bulletin, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_bulletin(request):
    if request.method == 'POST':
        serializer = BulletinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        bulletin = Bulletin.objects.filter(user_id=request.user.id)
        serializer = BulletinSerializer(bulletin, many=True)
        return Response(serializer.data)
    elif request.method == "PUT":
        bulletin = Bulletin.objects.get(pk=request.data["id"])
        serializer = BulletinSerializer(bulletin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        bulletin = Bulletin.objects.get(pk=request.data["id"])
        bulletin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

        