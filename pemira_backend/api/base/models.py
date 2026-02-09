import uuid

from django.db import models
from django.utils import timezone


def format_timestamp(timestamp):
    local_time = timestamp + timezone.timedelta(hours=7)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)

        self.save()

    def get_created_at(self):
        return format_timestamp(self.created_at)

    get_created_at.short_description = 'Created At'
    get_created_at.admin_order_field = 'created_at'

    def get_updated_at(self):
        return format_timestamp(self.updated_at)

    get_updated_at.short_description = 'Updated At'
    get_updated_at.admin_order_field = 'updated_at'

