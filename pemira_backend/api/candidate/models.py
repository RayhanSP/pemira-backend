from django.db import models

from pemira_backend.api.base.models import BaseModel
from pemira_backend.core.base.utilities.object_mapper_utility import ObjectMapperUtil
from pemira_backend.core.candidate.models import CandidatePairDomain


class CandidatePair(BaseModel):
    election_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    candidate_pair_photo = models.URLField(null=True, blank=True)
    president = models.CharField(max_length=255, null=True, blank=True)
    vice_president = models.CharField(max_length=255, null=True, blank=True)
    tagline = models.CharField(max_length=255, null=True, blank=True)
    vision = models.TextField(null=True, blank=True)
    mission = models.JSONField(default=list, blank=True, null=True)
    programs = models.JSONField(default=list, null=True, blank=True)
    social_media = models.URLField(null=True, blank=True)
    document_url = models.URLField(null=True, blank=True)
    is_empty_box = models.BooleanField(default=False)

    class Meta:
        db_table = "candidate_pairs"
        verbose_name = "Candidate Pair"

    def __str__(self):
        return f"{self.election_number} - {self.name}"

    def to_domain(self):
        domain = ObjectMapperUtil.map(self, CandidatePairDomain)
        return domain
