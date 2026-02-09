from dataclasses import dataclass


@dataclass
class VoteSpec:
    user_id: str
    candidate_id: str

@dataclass
class CountVoteResult:
    count: int

@dataclass
class RevealVoteItem:
    candidate_id: str
    candidate_name: str
    count: int

@dataclass
class RevealVoteResult:
    revealed_votes: list[RevealVoteItem]