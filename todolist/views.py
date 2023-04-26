from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response



# Create your views here.
class ToDoListView(APIView):
    def get(self, request):
        pass
    def post(self, request):
        pass
    
class ToDoListDetailView(APIView):
    def get(self, request, todolist_id):
        pass
    def post(self, request, todolist_id):
        pass
    def delete(self, request, todolist_id):
        pass