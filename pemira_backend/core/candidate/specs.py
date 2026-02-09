from dataclasses import dataclass
from typing import List


@dataclass
class GetCandidateItem:
    id: str
    election_number: int
    name: str
    candidate_pair_photo: str
    tagline: str
    president: str
    vice_president: str
    is_empty_box: bool

@dataclass
class GetCandidatesResult:
    candidates: List[GetCandidateItem]

@dataclass
class GetCandidateResult:
    id: str
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