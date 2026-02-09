from injector import Module, singleton

from pemira_backend.api.auth.accessors.auth_token_accessor import AuthTokenAccessor
from pemira_backend.api.auth.accessors.participant_accessor import ParticipantAccessor
from pemira_backend.api.auth.accessors.user_accessor import UserAccessor
from pemira_backend.api.auth.adapters.auth_provider import AuthProvider
from pemira_backend.core.auth.accessors.auth_token_accessor import IAuthTokenAccessor
from pemira_backend.core.auth.accessors.participant_accessor import IParticipantAccessor
from pemira_backend.core.auth.accessors.user_accessor import IUserAccessor
from pemira_backend.core.auth.ports.auth_provider import IAuthProvider


class AuthModule(Module):
    def configure(self, binder):
        binder.bind(IAuthProvider, to=AuthProvider, scope=singleton)
        binder.bind(IParticipantAccessor, to=ParticipantAccessor, scope=singleton)
        binder.bind(IUserAccessor, to=UserAccessor, scope=singleton)
        binder.bind(IAuthTokenAccessor, to=AuthTokenAccessor, scope=singleton)