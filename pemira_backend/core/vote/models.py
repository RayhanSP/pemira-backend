from dataclasses import dataclass

from pemira_backend.core.base.models import BaseDomain


@dataclass
class VoteDomain(BaseDomain):
    participant_id: str
    payload: str