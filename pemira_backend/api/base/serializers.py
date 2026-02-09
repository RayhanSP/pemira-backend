from rest_framework import serializers

from pemira_backend.core.base.constants import PAGINATION_DEFAULT_PAGE, PAGINATION_DEFAULT_SIZE

class PaginationRequest(serializers.Serializer):
    page = serializers.IntegerField(
        default=PAGINATION_DEFAULT_PAGE, allow_null=True, min_value=1
    )
    size = serializers.IntegerField(
        default=PAGINATION_DEFAULT_SIZE, allow_null=True, min_value=1
    )
    query = serializers.CharField(
        required=False, allow_null=True, allow_blank=True, min_length=1
    )

class PaginationResponse(serializers.Serializer):
    total_item = serializers.IntegerField()
    total_page = serializers.IntegerField()

class ExceptionResponse(serializers.Serializer):
    error_message = serializers.CharField()
    status_code = serializers.IntegerField()