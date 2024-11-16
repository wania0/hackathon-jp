from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Employeer").exists():
            return True
        return False
    
class IsJobSeeker(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Job Seeker").exists():
            return True
        return False