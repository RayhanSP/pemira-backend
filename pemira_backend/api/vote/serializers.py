from rest_framework import serializers

class VoteRequest(serializers.Serializer):
    candidate_id = serializers.UUIDField()

class CountVoteResponse(serializers.Serializer):
    count = serializers.IntegerField()

class RevealVoteItemResponse(serializers.Serializer):
    candidate_id = serializers.UUIDField()
    candidate_name = serializers.CharField()
    count = serializers.IntegerField()

class RevealVoteResponse(serializers.Serializer):
    revealed_votes = serializers.ListSerializer(child=RevealVoteItemResponse())