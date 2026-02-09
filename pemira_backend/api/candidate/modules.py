from injector import Module, singleton

from pemira_backend.api.candidate.accessors import CandidateAccessor
from pemira_backend.core.candidate.accessors import ICandidateAccessor


class CandidateModule(Module):
    def configure(self, binder):
        binder.bind(ICandidateAccessor, to=CandidateAccessor, scope=singleton)
