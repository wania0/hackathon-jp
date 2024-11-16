from django.db import models
from django.contrib.auth.models import User

class JobSeeker(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    qualification = models.CharField(max_length=500)
    cv = models.FileField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    profile_image = models.ImageField()


class Employeer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    company_size = models.IntegerField()
    logo = models.ImageField(null=True, blank=True)

class JobPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField(max_length=500, blank=True, null=True)
    required_skills = models.TextField(max_length=500, blank=True, null=True)
    salary_range = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20)
    posted_at = models.DateField()

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    submitted_at = models.DateField()
    
    def __str__(self):
        return self.job_post.job_title
    

   