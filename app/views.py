from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsEmployer, IsJobSeeker
from rest_framework.permissions import IsAuthenticated

from .models import JobSeeker, Employeer, JobPost, Application
from .serializers import JobSeekerSerializer, EmployeerSerializer, JobPostSerializerWithSalary, JobPostSerializerWithoutSalary, ApplicationSerializer
from .filters import JobPostFilter, EmployeerFilter
from .paginations import CustomPagination
    
class EmployeerGenericCreateUpdateApiView(CreateAPIView,UpdateAPIView):
    queryset = Employeer.objects.all()
    serializer_class = EmployeerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeerFilter

    def create(self, request, *args, **kwargs): # works before serializer validation

        if  Employeer.objects.filter(user=self.request.user).exists():
            print("user exists")
            return Response("already-created", status= status.HTTP_406_NOT_ACCEPTABLE)

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer): # works after serializer validation
        return Employeer.objects.create(user=self.request.user, **serializer.validated_data)

class JobPostModelViewSet(ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializerWithSalary
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobPostFilter
    pagination_class = CustomPagination
    
    def get_permissions(self):
        if self.action == "create":
            return [IsEmployer()]
        if self.action == "apply":
            return [IsJobSeeker()]
        return super().get_permissions()
    
    # create application for a specific job_post
    @action(detail=True, methods=["post"])
    def apply(self, request, pk=id):
        jobpost = JobPost.objects.get(id=pk)
        application = Application.objects.create(job_post=jobpost, job_seeker=request.user )#**serializer.validated_data )
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)
    
    # view applications for a specific job_post
    @action(detail=True, methods=["get"])
    def applications(self, request, pk=id):
        jobpost = JobPost.objects.get(id=pk)
        applications = Application.objects.filter(job_post=jobpost)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)


# each employeer can see only its own jobpost
    @action(detail=False, methods=["get"])
    def my_jobposts(self, request):
        user = self.request.user
        if not user.is_authenticated:
            return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        queryset = JobPost.objects.filter(user=user)
        serializer = JobPostSerializerWithSalary(queryset, many=True)
        return Response(serializer.data)
    
# update jobpost status
    @action(detail=True, methods=["put"])
    def update_jobpost(self, request, pk=id):
        jobpost = JobPost.objects.get(id=pk)
        if jobpost.status == 1:
            jobpost.status = 0
        else:
            jobpost.status = 1
        jobpost.save()
        return Response("success")
    
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return JobPostSerializerWithSalary
        else:
            return JobPostSerializerWithoutSalary
        
# 20 Latest Jobs: Displays the latest 20 jobs.
    @action(detail=False, methods = ['get'])
    def get_job_posts(self, request):
       latest_jobs = JobPost.objects.order_by('-posted_at')[0:20]
       serializer = JobPostSerializerWithSalary(latest_jobs, many=True)
       return Response(serializer.data)
   
class JobSeekerModelViewSet(ModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
    
# class ApplicationModelViewSet(ModelViewSet):
#     queryset = Application.objects.all()
#     serializer_class = ApplicationSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)