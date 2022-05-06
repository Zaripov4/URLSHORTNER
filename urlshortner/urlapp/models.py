import uuid
from datetime import datetime, timedelta
from django.db import models


def get_expire_date():
    return datetime.now() + timedelta(days=30)


def get_short():
    return str(uuid.uuid4())[:8]


class LinkInfo(models.Model):
    link = models.URLField(max_length=10000)
    short_link = models.CharField(max_length=8, default=get_short)
    expire_date = models.DateTimeField(default=get_expire_date)

    def __str__(self):
        return self.short_link
