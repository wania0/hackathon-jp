from django_filters import rest_framework as filters
from .models import JobPost, Employeer

class JobPostFilter(filters.FilterSet):
    job_title = filters.CharFilter(field_name="job_title", lookup_expr="icontains") # like
    # job_description = filters.CharFilter(field_name="job_description", lookup_expr="icontains") # like
    required_skills = filters.CharFilter(field_name="required_skills", lookup_expr="icontains") # like
    salary_min = filters.NumberFilter(field_name="salary_range", lookup_expr="gte") # greater than or equal to
    salary_max = filters.NumberFilter(field_name="salary_range", lookup_expr="lte") # less than or equal to
    status = filters.CharFilter(field_name="status", lookup_expr="exact") # where clause
    posted_after = filters.DateFilter(field_name="posted_at", lookup_expr="gte")  # greater than or equal to
    
    class Meta:
        model = JobPost
        fields = [
            "id",
            "user",
            "job_title",
            "job_description",
            "required_skills",
            "salary_range",
            "status",
            "posted_at"
        ]
        
class EmployeerFilter(filters.FilterSet):
    city = filters.CharFilter(field_name="city", lookup_expr="icontains") # like
    country = filters.CharFilter(field_name="country", lookup_expr="icontains") # like
    company_name = filters.CharFilter(field_name="company_name", lookup_expr="icontains") # like
    job_type = filters.CharFilter(field_name="jobpost__job_title", lookup_expr="icontains") # greater than or equal to
    
    class Meta:
        model = Employeer
        fields = [
            "city",
            "country",
            "company_name",
        ]