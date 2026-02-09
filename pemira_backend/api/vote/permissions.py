from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsCommittee(BasePermission):
    def has_permission(self, request: Request, view):
        group_names = [group.name for group in request.user.groups.all()]
        return 'committee' in group_names or request.user.is_superuser