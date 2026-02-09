from abc import ABC, abstractmethod
from typing import Optional

from pemira_backend.core.auth.models import UserDomain, ParticipantDomain
from pemira_backend.core.auth.specs import CreateParticipantSpec


class IParticipantAccessor(ABC):
    @abstractmethod
    def get_or_create(self, spec: CreateParticipantSpec) -> (Optional[ParticipantDomain], bool):
        raise NotImplementedError
    @abstractmethod
    def get_by_user_id(self, user_id: str) -> Optional[ParticipantDomain]:
        raise NotImplementedError