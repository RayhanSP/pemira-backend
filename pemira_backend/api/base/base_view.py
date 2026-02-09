from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ViewSet


class BaseViewSet(ViewSet):
    authenticated_actions = []

    def get_permissions(self):
        if self.action in self.authenticated_actions:
            self.permission_classes.insert(0, IsAuthenticated)
        else:
            self.permission_classes = [AllowAny, ]
        return super().get_permissions()