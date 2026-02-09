from django.db import models

from pemira_backend.api.auth.models import Participant
from pemira_backend.api.base.models import BaseModel
from pemira_backend.core.base.utilities.object_mapper_utility import ObjectMapperUtil
from pemira_backend.core.vote.models import VoteDomain


class Vote(BaseModel):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE, related_name="vote")
    payload = models.TextField()

    class Meta:
        db_table = "votes"
        verbose_name = "Vote"

    def __str__(self):
        return f"{self.participant}-{self.created_at}"

    def to_domain(self):
        return ObjectMapperUtil.map(self, VoteDomain)