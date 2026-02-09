from rest_framework import status
from rest_framework.renderers import JSONRenderer


class BaseJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code

        response_data = data

        response = {
            "is_success": True,
            "message": "Request successfully processed",
            "status_code": status_code,
            "content": response_data,
        }

        if status_code >= status.HTTP_400_BAD_REQUEST:
            response["is_success"] = False
            response["content"] = None
            response["message"] = response_data["error_message"]
            response["status_code"] = response_data["status_code"]

        return super(BaseJSONRenderer, self).render(
            response, accepted_media_type, renderer_context
        )