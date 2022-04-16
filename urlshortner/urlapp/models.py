from datetime import datetime

from django.db import models


class LinkInfo(models.Model):
    link = models.CharField(max_length=10000)
    link_id = models.CharField(max_length=8)

    def __str__(self):
        return self.link_id


def get_expire_date():
    return datetime.now() + timedelta(days=30)


class ExpireDate(models.Model):
    expire_date = models.DateTimeField(default=get_expire_date)


