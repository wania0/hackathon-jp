from .models import JobSeeker, Employeer, JobPost, Application
from rest_framework import serializers
from user_auth.serializers import UserSerializer

from enum import Enum

class EmployeerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    dob = serializers.DateField(format="%Y-%m-%d") 
    class Meta:
        model = Employeer 
        fields = "__all__" # all fields name
        
class StatusEnum(Enum):
    ENABLE = "enable"
    DISABLE = "disable"
    
class JobPostSerializerWithSalary(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    status = serializers.ChoiceField(choices=[(tag, tag.value) for tag in StatusEnum], read_only=True)
    class Meta:
        model =  JobPost
        fields = ['id', 'user', 'job_title', 'job_description', 'required_skills','status', 'posted_at']  # List all fields

    def create(self, validated_data):
        return JobPost.objects.create(**validated_data, user=self.context["request"].user)
    
class JobPostSerializerWithoutSalary(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    status = serializers.ChoiceField(choices=[(tag, tag.value) for tag in StatusEnum], read_only=True)
    class Meta:
        model =  JobPost
        fields = ["job_title", "job_description", "required_skills", "status", "user"]
    
class JobSeekerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = JobSeeker 
        fields = "__all__" # all fields name
    
class StatussEnum(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    HIRED = "hired"
    
class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    job_post = serializers.PrimaryKeyRelatedField(queryset=JobPost.objects.all(), source='JobPost')
    status = serializers.ChoiceField(choices=[(tag.value, tag.value) for tag in StatussEnum], read_only = True)
    class Meta:
        model = Application
        fields = ['id', 'user', 'job_post', 'submitted_at', 'status']
    
    