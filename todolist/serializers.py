from rest_framework import serializers
import datetime
from todolist.models import ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = ToDoList
        fields = ['user', 'title', 'content', 'is_done']
class ToDoListCreateSerializer(serializers.ModelSerializer):  
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = ToDoList
        fields = ['user', 'title', 'content', 'is_complete']
        

class ToDoListPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['is_done', 'is_complete']
        
    def update(self, instance, validated_data):
        instance.is_done = validated_data.get('is_done', instance.is_done)
        if instance.is_done==True:
            instance.completion_at = datetime.datetime.now()
        instance.save()
        return instance