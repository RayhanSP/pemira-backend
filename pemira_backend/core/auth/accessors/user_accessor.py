from abc import ABC, abstractmethod
from typing import Optional

from pemira_backend.core.auth.models import UserDomain
from pemira_backend.core.auth.specs import CreateUserSpec


class IUserAccessor(ABC):
    @abstractmethod
    def get_or_create(self, spec: CreateUserSpec) -> (Optional[UserDomain], bool):
        raise NotImplementedError
