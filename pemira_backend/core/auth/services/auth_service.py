from datetime import timedelta, datetime

from django.utils.timezone import now
from injector import inject

from pemira_backend.core.auth.accessors.auth_token_accessor import IAuthTokenAccessor
from pemira_backend.core.auth.accessors.participant_accessor import IParticipantAccessor
from pemira_backend.core.auth.accessors.user_accessor import IUserAccessor
from pemira_backend.core.auth.ports.auth_provider import IAuthProvider
from pemira_backend.core.auth.specs import LoginSpec, CreateUserSpec, CreateParticipantSpec, CreateAuthTokenSpec, \
    LoginResult
from pemira_backend.core.vote.accessors import IVoteAccessor


class AuthService:
    @inject
    def __init__(
        self,
        participant_accessor: IParticipantAccessor,
        user_accessor: IUserAccessor,
        auth_token_accessor: IAuthTokenAccessor,
        auth_provider:IAuthProvider,
        vote_accessor: IVoteAccessor
    ):
        self.participant_accessor = participant_accessor
        self.user_accessor = user_accessor
        self.auth_token_accessor = auth_token_accessor
        self.auth_provider = auth_provider
        self.vote_accessor = vote_accessor

    def authenticate(self, spec: LoginSpec):
        user, _ = self.user_accessor.get_or_create(
            CreateUserSpec(
                email=spec.email,
                name=spec.name,
            )
        )

        participant, _ = self.participant_accessor.get_or_create(
            CreateParticipantSpec(
                user_id=user.id,
                major=spec.major,
                npm=spec.npm
            )
        )

        auth_token = self.auth_provider.generate_token()
        expired_at = now() + timedelta(
            minutes=15
        )

        token = self.auth_token_accessor.upsert(
            CreateAuthTokenSpec(
                user_id=user.id,
                key=auth_token,
                expired_at=expired_at,
            )
        )

        return LoginResult(
            id=user.id,
            email=user.email,
            name=user.name,
            token=token.key,
            npm=participant.npm,
            major=participant.major,
            batch=participant.batch,
        )

