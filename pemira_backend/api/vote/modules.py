from injector import Module, singleton

from pemira_backend.api.vote.accessors import VoteAccessor
from pemira_backend.api.vote.adapters.cipher_provider import CipherProvider
from pemira_backend.core.vote.accessors import IVoteAccessor
from pemira_backend.core.vote.ports.cipher_provider import ICipherProvider


class VoteModule(Module):
    def configure(self, binder):
        binder.bind(ICipherProvider, to=CipherProvider, scope=singleton)
        binder.bind(IVoteAccessor, to=VoteAccessor, scope=singleton)
