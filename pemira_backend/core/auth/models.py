from dataclasses import dataclass
from datetime import datetime

from pemira_backend.core.base.models import BaseDomain


@dataclass
class UserDomain(BaseDomain):
    name: str
    email: str
    is_staff: bool
    is_active: bool
    password: str

@dataclass
class ParticipantDomain(BaseDomain):
    npm: str
    batch: str
    major: str
    user_id: str

@dataclass
class AuthTokenDomain(BaseDomain):
    key: str
    user_id: str
    expired_at: datetime