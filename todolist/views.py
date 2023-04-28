from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from todolist.models import ToDoList
from todolist.serializers import ToDoListSerializer, ToDoListCreateSerializer, ToDoListPutSerializer


# Create your views here.
class ToDoListView(APIView):
    def get(self, request):
        todolist = ToDoList.objects.all()
        serializer = ToDoListSerializer(todolist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ToDoListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ToDoListDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, todolist_id):
        todolist = get_object_or_404(ToDoList, id=todolist_id)
        serializer = ToDoListSerializer(todolist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, todolist_id):
        todolist = get_object_or_404(ToDoList, id=todolist_id)
        if request.user == todolist.user:
            
            serializer = ToDoListPutSerializer(todolist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, todolist_id):
        todolist = get_object_or_404(ToDoList, id=todolist_id)
        if request.user == todolist.user:
            todolist.delete()
            return Response("삭제되었습니다.", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
            