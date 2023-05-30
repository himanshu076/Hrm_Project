from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.schemas import DefaultSchema

from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.views import APIView


# Create your views here.
class UserModelApiView(APIView):
    schema = AutoSchema()
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            user = User.objects.get(pk=id)
            Serializer = UserSerializer(user)
            return Response(Serializer.data)

        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = User(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'User Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        user = User.objects.get(pk=id)
        serializer = User(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        user = User.objects.get(pk=id)
        user.delete()
        return Response({'msg':'Data Deleated'})
