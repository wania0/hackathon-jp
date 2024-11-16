from rest_framework import serializers
from django.contrib.auth.models import Group, User
from enum import Enum
class StatusEnum(Enum):
    JOB_SEEKER = "Job Seeker"
    EMPLOYEER = "Employeer"
   

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[(tag, tag.value) for tag in StatusEnum], read_only=True)
    

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField(read_only=True) 
