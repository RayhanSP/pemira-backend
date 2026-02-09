import json
from collections import defaultdict
from dataclasses import asdict
from http import HTTPStatus
from typing import List

from injector import inject

from pemira_backend.api.base.utilities.base_exception_handler import CommonException
from pemira_backend.core.auth.accessors.participant_accessor import IParticipantAccessor
from pemira_backend.core.base.utilities.dictionary_utility import DictionaryUtil
from pemira_backend.core.base.utilities.object_mapper_utility import ObjectMapperUtil
from pemira_backend.core.candidate.accessors import ICandidateAccessor
from pemira_backend.core.candidate.models import CandidatePairDomain
from pemira_backend.core.vote.accessors import IVoteAccessor
from pemira_backend.core.vote.ports.cipher_provider import ICipherProvider
from pemira_backend.core.vote.specs import VoteSpec, CountVoteResult, RevealVoteResult, RevealVoteItem


class VoteService:
    @inject
    def __init__(
        self,
        vote_accessor: IVoteAccessor,
        participant_accessor: IParticipantAccessor,
        candidate_accessor: ICandidateAccessor,
        cipher_provider: ICipherProvider
    ):
        self.vote_accessor = vote_accessor
        self.participant_accessor = participant_accessor
        self.candidate_accessor = candidate_accessor
        self.cipher_provider = cipher_provider

    def check_voting_status(self, user_id: str):
        participant = self.participant_accessor.get_by_user_id(
            user_id=user_id
        )

        if participant is None:
            raise CommonException("Participant not found", HTTPStatus.FORBIDDEN)

        vote = self.vote_accessor.find_by_participant_id(
            participant_id=participant.id
        )

        return vote is not None

    def vote(self, vote_spec: VoteSpec):
        participant = self.participant_accessor.get_by_user_id(
            user_id=vote_spec.user_id
        )

        if participant is None:
            raise CommonException("Participant not found", HTTPStatus.NOT_FOUND)

        candidate = self.candidate_accessor.find_by_id(
            candidate_id=vote_spec.candidate_id
        )

        if candidate is None:
            raise CommonException("Candidate not found", HTTPStatus.NOT_FOUND)


        payload = self.cipher_provider.encrypt(
            json.dumps(
                DictionaryUtil.transform_into_jsonable_dictionary(asdict(candidate))
            )
        )

        self.vote_accessor.create(
            participant_id=participant.id,
            payload=payload
        )

    def count_vote(self):
        votes = self.vote_accessor.find_all()
        return CountVoteResult(
            count=len(votes)
        )

    def reveal_vote(self):
        votes = self.vote_accessor.find_all()

        decrypted_candidates = [
            json.loads(
                self.cipher_provider.decrypt(vote.payload)
            )
            for vote in votes
        ]

        candidates = [
            ObjectMapperUtil.map(candidate, CandidatePairDomain)
            for candidate in decrypted_candidates
        ]

        revealed_votes = defaultdict(lambda: {"candidate_id": "", "count": 0})
        for candidate in candidates:
            if revealed_votes[candidate.name]["candidate_id"] == "":
                revealed_votes[candidate.name]["candidate_id"] = candidate.id
            revealed_votes[candidate.name]["count"] += 1

        return RevealVoteResult(
            revealed_votes=[
                RevealVoteItem(
                    candidate_id=value.get("candidate_id"),
                    candidate_name=key,
                    count=value.get("count"),
                )
                for key, value in revealed_votes.items()
            ]
        )