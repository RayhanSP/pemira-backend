from http import HTTPStatus

from django.conf import settings
from injector import inject

from pemira_backend.api.base.utilities.base_exception_handler import CommonException
from pemira_backend.core.candidate.accessors import ICandidateAccessor
from pemira_backend.core.candidate.specs import GetCandidatesResult, GetCandidateItem, GetCandidateResult


class CandidateService:
    @inject
    def __init__(self, candidate_accessor: ICandidateAccessor):
        self.candidate_accessor = candidate_accessor

    def get_candidates(self):
        candidate_pairs = self.candidate_accessor.find_all()

        return GetCandidatesResult(
            candidates=[
                GetCandidateItem(
                    id=candidate_pair.id,
                    election_number=candidate_pair.election_number,
                    name=candidate_pair.name,
                    candidate_pair_photo=candidate_pair.candidate_pair_photo,
                    tagline=candidate_pair.tagline,
                    president=candidate_pair.president,
                    vice_president=candidate_pair.vice_president,
                    is_empty_box=candidate_pair.is_empty_box,
                )
                for candidate_pair in candidate_pairs
            ]
        )

    def get_candidate(self, candidate_id: str):
        candidate = self.candidate_accessor.find_by_id(candidate_id)

        if candidate is None:
            raise CommonException("Candidate not found", HTTPStatus.NOT_FOUND)

        return GetCandidateResult(
            id=candidate.id,
            election_number=candidate.election_number,
            name=candidate.name,
            candidate_pair_photo=candidate.candidate_pair_photo,
            president=candidate.president,
            vice_president=candidate.vice_president,
            tagline=candidate.tagline,
            vision=candidate.vision,
            mission=candidate.mission,
            programs=candidate.programs,
            social_media=candidate.social_media,
            document_url=candidate.document_url,
        )