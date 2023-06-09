from .models import User
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer

# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"회원가입 완료-옷~"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class ToDoListUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
    
    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'저리가.. 권한x'}, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            user.delete()
        return Response({'message': 'user 정보가 삭제되었습니다.'})
    