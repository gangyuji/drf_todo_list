from django.db import models
from users.models import User

# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    is_complete = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title