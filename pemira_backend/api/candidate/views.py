from dataclasses import asdict

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from pemira_backend.api.base.base_view import BaseViewSet
from pemira_backend.api.candidate.serializers import GetCandidatesResponse, GetCandidateRequest, GetCandidateResponse
from pemira_backend.api.modules import injector
from pemira_backend.core.base.utilities.dictionary_utility import DictionaryUtil
from pemira_backend.core.candidate.services import CandidateService

candidate_service = injector.get(CandidateService)

class CandidateView(BaseViewSet):
    @action(detail=False, methods=["GET"], url_path="list")
    def get_candidates(self, request: Request):
        result = candidate_service.get_candidates()
        return Response(
            GetCandidatesResponse(
                DictionaryUtil.transform_into_jsonable_dictionary(asdict(result))
            ).data,
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["GET"], url_path="get")
    def get_candidate_detail(self, request: Request):
        serializer = GetCandidateRequest(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        result = candidate_service.get_candidate(serializer.validated_data.get("candidate_id"))
        return Response(
            GetCandidateResponse(
                DictionaryUtil.transform_into_jsonable_dictionary(asdict(result))
            ).data,
            status=status.HTTP_200_OK,
       )