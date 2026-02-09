from rest_framework import serializers

class GetCandidate(serializers.Serializer):
    id = serializers.UUIDField()
    election_number = serializers.IntegerField()
    name = serializers.CharField()
    candidate_pair_photo = serializers.CharField()
    tagline = serializers.CharField()
    president = serializers.CharField()
    vice_president = serializers.CharField()
    is_empty_box = serializers.BooleanField()

class GetCandidatesResponse(serializers.Serializer):
    candidates = serializers.ListSerializer(child=GetCandidate())

class GetCandidateRequest(serializers.Serializer):
    candidate_id = serializers.UUIDField()

class GetCandidateResponse(serializers.Serializer):
    id = serializers.UUIDField()
    election_number = serializers.IntegerField()
    name = serializers.CharField()
    candidate_pair_photo = serializers.CharField()
    president = serializers.CharField()
    vice_president = serializers.CharField()
    tagline = serializers.CharField()
    vision = serializers.CharField()
    mission = serializers.ListSerializer(child=serializers.CharField())
    programs = serializers.ListSerializer(child=serializers.CharField())
    social_media = serializers.URLField()
    document_url = serializers.URLField()