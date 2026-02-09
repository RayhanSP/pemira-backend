from typing import List, Optional

from pemira_backend.api.vote.models import Vote
from pemira_backend.core.vote.accessors import IVoteAccessor
from pemira_backend.core.vote.models import VoteDomain


class VoteAccessor(IVoteAccessor):
    def find_all(self) -> List[VoteDomain]:
        vote_qs = Vote.objects.get_queryset().all()

        return [vote.to_domain() for vote in vote_qs]

    def create(self, participant_id: str, payload: str):
        Vote(participant_id=participant_id, payload=payload).save()

    def find_by_participant_id(self, participant_id: str) -> Optional[VoteDomain]:
        vote = Vote.objects.get_queryset().filter(participant_id=participant_id).first()

        if vote is None:
            return None

        return vote.to_domain()
