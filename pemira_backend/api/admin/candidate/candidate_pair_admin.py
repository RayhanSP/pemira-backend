from django.contrib.admin import ModelAdmin


class CandidatePairAdmin(ModelAdmin):
    list_display = ['election_number', 'president', 'vice_president', 'tagline']
    fieldsets = (
        ("", {
            "fields": [
                "election_number", "name", "is_empty_box", "president", "vice_president", "candidate_pair_photo",
                "tagline", "vision", "mission", "programs", "social_media", "document_url"
            ]
        }),
    )