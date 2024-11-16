from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmployeerGenericCreateUpdateApiView, JobPostModelViewSet, JobSeekerModelViewSet


router = DefaultRouter()
router.register("job-post", JobPostModelViewSet),
router.register("job-seeker", JobSeekerModelViewSet),
# router.register("application", ApplicationModelViewSet)

urlpatterns = [
    path('employeer/profile/', EmployeerGenericCreateUpdateApiView.as_view())

] + router.urls

