from dataclasses import asdict

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from pemira_backend.api.auth.serializers import LoginRequest, LoginResponse
from pemira_backend.api.base.base_view import BaseViewSet
from pemira_backend.api.modules import injector
from pemira_backend.core.auth.services.auth_service import AuthService
from pemira_backend.core.auth.specs import LoginSpec
from pemira_backend.core.base.utilities.dictionary_utility import DictionaryUtil
from pemira_backend.core.base.utilities.object_mapper_utility import ObjectMapperUtil

auth_service = injector.get(AuthService)

class AuthView(BaseViewSet):
    @action(detail=False, methods=["POST"], url_path="login")
    def login(self, request: Request):
        serializer = LoginRequest(data=request.data)
        serializer.is_valid(raise_exception=True)
        spec = ObjectMapperUtil.map(serializer.validated_data, LoginSpec)
        result = auth_service.authenticate(spec)
        return Response(
            LoginResponse(
                DictionaryUtil.transform_into_jsonable_dictionary(asdict(result))
            ).data,
            status=status.HTTP_200_OK,
        )
