from dataclasses import dataclass
from datetime import datetime


@dataclass
class LoginSpec:
    email: str
    name: str
    npm: str
    major: str

@dataclass
class LoginResult:
    id: str
    email: str
    name: str
    npm: str
    major: str
    batch: str
    token: str

@dataclass
class CreateUserSpec:
    email: str
    name: str

@dataclass
class CreateParticipantSpec:
    user_id: str
    npm: str
    major: str

@dataclass
class CreateAuthTokenSpec:
    key: str
    user_id: str
    expired_at: datetime