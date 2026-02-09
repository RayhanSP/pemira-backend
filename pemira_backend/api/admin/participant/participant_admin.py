from django.contrib.admin import ModelAdmin, action

from pemira_backend.api.auth.models import Participant


class ParticipantAdmin(ModelAdmin):
    list_display = ["get_participant_name", "get_participant_email", "npm", "batch", "major", "get_participant_last_login"]

    @action(description="Name")
    def get_participant_name(self, obj: Participant):
        return obj.user.name

    @action(description="Email")
    def get_participant_email(self, obj: Participant):
        return obj.user.email

    @action(description="Last Login")
    def get_participant_last_login(self, obj: Participant):
        return obj.user.last_login
