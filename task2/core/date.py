from django.db import models


class DateParent(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField()

    class Meta:
        abstract = True
