from django.db import models
from django.contrib.auth.models import AbstractUser


class StatusChoice(models.TextChoices):
    status1 = 'none', 'none'
    status2 = 'educating', 'educating'
    status3 = 'working', 'working'


class RankChoices(models.TextChoices):
    rank1 = 'Freshman', 'Freshman'
    rank2 = 'Middle', 'Middle'
    rank3 = 'Experienced', 'Experienced'


class UserProfile(AbstractUser):
    status = models.CharField(max_length=9, choices=StatusChoice.choices, default=StatusChoice.status1)
    rank = models.CharField(max_length=11, choices=RankChoices.choices, default=RankChoices.rank1)

    avatar = models.ImageField(null=True)
    place_of_employment = models.CharField(max_length=255, null=True)
    about_yourself = models.TextField(null=True)
    location = models.CharField(max_length=255, null=True)
    rating = models.IntegerField(default=10)

    # def status_mapping(self, status):
    #     status_mapping = {
    #         'none': StatusChoice.status1,
    #         'educating': StatusChoice.status2,
    #         'working': StatusChoice.status3
    #     }
    #     if status:
    #         return status_mapping.get(status, StatusChoices.status1)
    #     return StatusChoices.status1
    #
    # status = self.status_mapping(self._data.get('status', {}).get('status'))