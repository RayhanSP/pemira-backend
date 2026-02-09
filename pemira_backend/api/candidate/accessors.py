from typing import List, Optional

from pemira_backend.api.candidate.models import CandidatePair
from pemira_backend.core.candidate.accessors import ICandidateAccessor
from pemira_backend.core.candidate.models import CandidatePairDomain


class CandidateAccessor(ICandidateAccessor):
    def find_all(self) -> List[CandidatePairDomain]:
        qs = CandidatePair.objects.get_queryset().order_by('election_number').all()

        return [candidate.to_domain() for candidate in qs]

    def find_by_id(self, candidate_id: str) -> Optional[CandidatePairDomain]:
        try:
            qs = CandidatePair.objects.get_queryset().get(id=candidate_id)

            return qs.to_domain()
        except CandidatePair.DoesNotExist:
            return None

