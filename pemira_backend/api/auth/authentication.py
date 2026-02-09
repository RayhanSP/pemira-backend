from datetime import datetime, timedelta

from django.utils.timezone import now
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from pemira_backend.api.auth.models import AuthToken


class UserExpiringTokenAuthentication(TokenAuthentication):
    model = AuthToken
    keyword = "Bearer"

    def authenticate_credentials(self, key):
        auth_token = self.get_model()

        token = auth_token.objects.filter(key=key).first()
        if token is None:
            raise exceptions.AuthenticationFailed()

        user = token.user
        if not user.is_active:
            raise exceptions.AuthenticationFailed()

        if self._is_token_expired(token):
            token.delete()
            raise exceptions.AuthenticationFailed()

        token.expired_at = self.get_new_token_expiration_time(token.expired_at)
        token.save()
        return user, token

    @staticmethod
    def _is_token_expired(token) -> bool:
        return token.expired_at < now()

    @staticmethod
    def get_new_token_expiration_time(current_expiration_time: datetime) -> datetime:
        next_hour = now() + timedelta(hours=1)
        return max(current_expiration_time, next_hour)