from django.db import models


class LinkInfo(models.Model):
    link = models.CharField(max_length=10000)
    link_id = models.CharField(max_length=8)

    def __str__(self):
        return self.link_id
