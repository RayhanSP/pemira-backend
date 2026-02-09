from dataclasses import dataclass
from typing import Optional

from rest_framework import status

from pemira_backend.core.base.constants import JSON_FIELD_OPTION_TYPES


@dataclass
class BaseResponseSpec:
    message: str
    content: JSON_FIELD_OPTION_TYPES
    status_code: Optional[int] = status.HTTP_200_OK
    is_success: Optional[bool] = True

@dataclass
class PaginationSpec:
    size: int
    page: int
    query: Optional[str]

@dataclass
class PaginationResult:
    total_item: int
    total_page: int

@dataclass
class ExceptionResult:
    status_code: int
    error_message: str