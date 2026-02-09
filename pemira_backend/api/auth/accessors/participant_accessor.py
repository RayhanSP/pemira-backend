from typing import Optional

from pemira_backend.api.auth.models import Participant
from pemira_backend.core.auth.accessors.participant_accessor import IParticipantAccessor
from pemira_backend.core.auth.models import ParticipantDomain
from pemira_backend.core.auth.specs import CreateParticipantSpec


class ParticipantAccessor(IParticipantAccessor):
    def get_or_create(self, spec: CreateParticipantSpec) -> (Optional[ParticipantDomain], bool):
        participant_qs, created = Participant.objects.get_queryset().get_or_create(
            user_id=spec.user_id,
            defaults={
                'npm': spec.npm,
                'major': spec.major,
                'user_id': spec.user_id,
            }
        )

        return participant_qs.to_domain(), created

    def get_by_user_id(self, user_id: str) -> Optional[ParticipantDomain]:
        qs = Participant.objects.get_queryset().filter(user_id=user_id).first()

        if qs is None:
            return None

        return qs.to_domain()
