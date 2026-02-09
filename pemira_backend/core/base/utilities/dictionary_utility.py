import dataclasses
import uuid
from datetime import datetime, time, date
from decimal import Decimal
from enum import Enum
from typing import Dict, Any, Optional, TypeVar, List

from django.db.models.fields.files import ImageFieldFile, FieldFile


class DictionaryUtil:
    @staticmethod
    def transform_into_jsonable_dictionary(
        data_object: Dict[str, Any], datetime_format: Optional[str] = None, tzinfo=None
    ) -> Optional[Dict[str, Any]]:
        if not isinstance(data_object, Dict):
            return None

        T = TypeVar("T")

        def transform_data(data: T) -> T:
            if isinstance(data, Enum):
                data = data.value
            elif isinstance(data, Decimal):
                data = float(data)
            elif isinstance(data, uuid.UUID):
                data = str(data)
            elif isinstance(data, datetime):
                if datetime_format:
                    data = data.strftime(datetime_format)
                else:
                    data = data.astimezone(tz=tzinfo).isoformat()
            elif isinstance(data, time):
                data = data.isoformat()
            elif isinstance(data, ImageFieldFile):
                data = str(data)
            elif isinstance(data, FieldFile):
                data = str(data)
            elif isinstance(data, date):
                data = data.isoformat()
            elif isinstance(data, List):
                for index in range(len(data)):
                    data[index] = transform_data(data[index])
            elif isinstance(data, Dict):
                for key in data:
                    data[key] = transform_data(data[key])
            elif dataclasses.is_dataclass(data):
                data = transform_data(dataclasses.asdict(data))

            return data

        return transform_data(data_object)