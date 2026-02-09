from abc import ABC, abstractmethod

from pemira_backend.core.auth.models import AuthTokenDomain
from pemira_backend.core.auth.specs import CreateAuthTokenSpec


class IAuthTokenAccessor(ABC):
    @abstractmethod
    def upsert(self, spec: CreateAuthTokenSpec) -> AuthTokenDomain:
        raise NotImplementedError