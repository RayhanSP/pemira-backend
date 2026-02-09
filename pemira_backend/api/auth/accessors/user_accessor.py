from typing import Optional

from pemira_backend.api.auth.models import User
from pemira_backend.core.auth.accessors.user_accessor import IUserAccessor
from pemira_backend.core.auth.models import UserDomain
from pemira_backend.core.auth.specs import CreateUserSpec


class UserAccessor(IUserAccessor):
    def get_or_create(self, spec: CreateUserSpec) -> (Optional[UserDomain], bool):
        user_qs, created = User.objects.get_queryset().get_or_create(
            email=spec.email,
            defaults={
                'email': spec.email,
                'name': spec.name,
            }
        )

        return user_qs.to_domain(), created
