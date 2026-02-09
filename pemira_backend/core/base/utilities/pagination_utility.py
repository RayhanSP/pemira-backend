import math
from typing import Tuple


class PaginationUtil:
    @classmethod
    def paginate(cls, size: int, total_data: int, page: int) -> Tuple[int, int, int]:
        total_page = math.ceil(total_data / size)
        start_index = size * (page - 1)
        end_index = start_index + size
        return total_page, start_index, end_index