from dataclasses import asdict

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from pemira_backend.api.base.base_view import BaseViewSet
from pemira_backend.api.modules import injector
from pemira_backend.api.vote.permissions import IsCommittee
from pemira_backend.api.vote.serializers import VoteRequest, CountVoteResponse, RevealVoteResponse
from pemira_backend.core.base.utilities.dictionary_utility import DictionaryUtil
from pemira_backend.core.base.utilities.object_mapper_utility import ObjectMapperUtil
from pemira_backend.core.vote.services import VoteService
from pemira_backend.core.vote.specs import VoteSpec

vote_service = injector.get(VoteService)

class VoteView(BaseViewSet):
    authenticated_actions = ["check_voting_status", "submit_vote", "reveal_vote"]

    @action(detail=False, methods=["GET"], url_path="check-status")
    def check_voting_status(self, request: Request):
        result = vote_service.check_voting_status(request.user.id)
        return Response(
            {'is_voted': result},
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["POST"], url_path="submit")
    def submit_vote(self, request: Request):
        serializer = VoteRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        spec = ObjectMapperUtil.map(serializer.validated_data, VoteSpec)
        spec.user_id = request.user.id

        vote_service.vote(spec)
        return Response(
            None,
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["GET"], url_path="count")
    def count_vote(self, request: Request):
        result = vote_service.count_vote()
        return Response(
            CountVoteResponse(
                DictionaryUtil.transform_into_jsonable_dictionary(asdict(result))
            ).data,
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["GET"], url_path="reveal", permission_classes=[IsCommittee])
    def reveal_vote(self, request: Request):
        result = vote_service.reveal_vote()
        return Response(
            RevealVoteResponse(
                DictionaryUtil.transform_into_jsonable_dictionary(asdict(result))
            ).data,
            status=status.HTTP_200_OK,
        )