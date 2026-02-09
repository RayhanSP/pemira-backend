from decimal import Decimal
from typing import Optional, Union, Dict, List, Any

SINGLE_VALUE_JSON_FIELD_TYPES = Optional[Union[str, int, float, Decimal, bool]]
JSON_FIELD_OPTION_TYPES = Union[
    Dict[Any, Any],
    List[SINGLE_VALUE_JSON_FIELD_TYPES],
    SINGLE_VALUE_JSON_FIELD_TYPES,
]
PAGINATION_DEFAULT_SIZE = 20
PAGINATION_DEFAULT_PAGE = 1