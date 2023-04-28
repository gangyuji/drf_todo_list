from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username', 'password', 'age', 'gender','introduction'] 
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def create(self, validated_data):
        user = super().create(validated_data)
        print(validated_data)
        password = user.password
   
        user.set_password(password)

        user.save()
        return user
    
    def update(self, obj, validated_data):
        # user = super().create(validated_data)
        # password = user.password
        # user.set_password(password)
        # user.save()
        obj.email = validated_data.get('email', obj.email)
        obj.username = validated_data.get('username', obj.username)
        obj.password = validated_data.get('password', obj.password)
        obj.age = validated_data.get('age', obj.age)
        obj.introduction = validated_data.get('introduction', obj.introduction)
        obj.save()
        return obj
    



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        token['username'] = user.username        
        token['email'] = user.email
        token['gender'] = user.gender
        token['age'] = user.age


        return token