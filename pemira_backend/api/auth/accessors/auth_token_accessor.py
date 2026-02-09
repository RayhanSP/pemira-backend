from pemira_backend.api.auth.models import AuthToken
from pemira_backend.core.auth.accessors.auth_token_accessor import IAuthTokenAccessor
from pemira_backend.core.auth.models import AuthTokenDomain
from pemira_backend.core.auth.specs import CreateAuthTokenSpec


class AuthTokenAccessor(IAuthTokenAccessor):
    def upsert(self, spec: CreateAuthTokenSpec) -> AuthTokenDomain:
        token, _ = AuthToken.objects.update_or_create(
            key=spec.key, defaults={
                'key': spec.key,
                'user_id': spec.user_id,
                'expired_at': spec.expired_at,
            }
        )
        return token.to_domain()