from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from pemira_backend.api.auth.managers import UserManager
from pemira_backend.api.base.models import BaseModel
from pemira_backend.core.auth.models import UserDomain, ParticipantDomain, AuthTokenDomain
from pemira_backend.core.base.utilities.object_mapper_utility import ObjectMapperUtil


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=256, null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = "User"

    def __str__(self):
        return f"{self.email}-{self.name}"

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    def to_domain(self):
        return ObjectMapperUtil.map(self, UserDomain)

class Participant(BaseModel):
    npm = models.CharField(max_length=10)
    batch = models.CharField(max_length=4)
    major = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="participant")

    class Meta:
        db_table = "participants"
        verbose_name = "Participant"

    def __str__(self):
        return f"{self.npm}-{self.user.name}"

    def save(self, *args, **kwargs):
        self.batch = f"20{self.npm[:2]}"
        super(Participant, self).save(*args, **kwargs)

    def to_domain(self):
        return ObjectMapperUtil.map(self, ParticipantDomain)

class AuthToken(BaseModel):
    key = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(
        User, related_name="auth_tokens", on_delete=models.CASCADE
    )
    expired_at = models.DateTimeField()

    class Meta:
        db_table = "auth_token"

    def __str__(self):
        return str(self.key)

    def to_domain(self):
        return ObjectMapperUtil.map(self, AuthTokenDomain)