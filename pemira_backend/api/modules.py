from injector import Injector

from pemira_backend.api.auth.modules import AuthModule
from pemira_backend.api.candidate.modules import CandidateModule
from pemira_backend.api.vote.modules import VoteModule

injector = Injector([
    AuthModule,
    CandidateModule,
    VoteModule
])