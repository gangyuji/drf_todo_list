from rest_framework import serializers

from todolist.models import ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = ToDoList
        fields = ['user', 'title', 'content', 'is_complete']
class ToDoListCreateSerializer(serializers.ModelSerializer):  
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = ToDoList
        fields = ['user', 'title', 'content', 'is_complete']