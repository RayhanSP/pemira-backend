from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.request import Request

from pemira_backend.api.base.base_view import BaseViewSet


class IndexView(BaseViewSet):

    @action(detail=False)
    def list(self, _request: Request):
        return HttpResponse("OK")
