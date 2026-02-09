from abc import ABC, abstractmethod
from typing import List, Optional

from pemira_backend.core.candidate.models import CandidatePairDomain


class ICandidateAccessor(ABC):
    @abstractmethod
    def find_all(self) -> List[CandidatePairDomain]:
        raise NotImplementedError
    @abstractmethod
    def find_by_id(self, candidate_id: str) -> Optional[CandidatePairDomain]:
        raise NotImplementedError