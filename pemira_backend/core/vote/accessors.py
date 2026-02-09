from abc import ABC, abstractmethod
from typing import List, Optional

from pemira_backend.core.vote.models import VoteDomain


class IVoteAccessor(ABC):
    @abstractmethod
    def create(self, participant_id: str, payload: str):
        raise NotImplementedError
    @abstractmethod
    def find_all(self) -> List[VoteDomain]:
        raise NotImplementedError
    @abstractmethod
    def find_by_participant_id(self, participant_id: str) -> Optional[VoteDomain]:
        raise NotImplementedError
