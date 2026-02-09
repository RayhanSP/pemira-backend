from dataclasses import dataclass
from typing import List

from pemira_backend.core.base.models import BaseDomain


@dataclass
class CandidatePairDomain(BaseDomain):
    election_number: int
    name: str
    candidate_pair_photo: str
    president: str
    vice_president: str
    tagline: str
    vision: str
    mission: List[str]
    programs: List[str]
    social_media: str
    document_url: str
    is_empty_box: bool