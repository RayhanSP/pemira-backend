from django.contrib.admin import AdminSite
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

from pemira_backend.api.admin.candidate.candidate_pair_admin import CandidatePairAdmin
from pemira_backend.api.admin.participant.participant_admin import ParticipantAdmin
from pemira_backend.api.admin.user.user_admin import UserAdmin
from pemira_backend.api.auth.models import User, Participant
from pemira_backend.api.candidate.models import CandidatePair

ADMIN_MENU_GROUPING = {
    "Account": [User, Participant, Group],
    "Candidate": [CandidatePair],
}

class PemiraAdminSite(AdminSite):
    site_header = "Pemira Admin"
    site_title = "Pemira Admin"
    index_title = "Hello!"

    def get_app_list(self, request, app_label=None):
        app_list = super().get_app_list(request, app_label)
        api_app = None

        for app in app_list:
            if app["app_label"] == "api":
                api_app = app
                app_list.remove(app)
                break

        if not api_app:
            return app_list

        misc_models = list(api_app["models"])
        for key, models in ADMIN_MENU_GROUPING.items():
            app_dict = {
                "name": key,
                "app_label": key.lower(),
                "app_url": "/admin/api/",
                "has_module_perms": True,
                "models": [],
            }

            for model in models:
                for m in api_app["models"]:
                    if m["model"] == model:
                        app_dict["models"].append(m)
                        if m in misc_models:
                            misc_models.remove(m)
                        break

            app_list.append(app_dict)

        misc_app_dict = {
            "name": "Misc",
            "app_label": "misc",
            "app_url": "/admin/api/",
            "has_module_perms": True,
            "models": misc_models,
        }

        app_list.append(misc_app_dict)

        return app_list

pemira_admin_site = PemiraAdminSite()
pemira_admin_site.register(User, UserAdmin)
pemira_admin_site.register(Group, GroupAdmin)
pemira_admin_site.register(Participant, ParticipantAdmin)
pemira_admin_site.register(CandidatePair, CandidatePairAdmin)