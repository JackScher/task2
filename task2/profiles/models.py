from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    avatar = models.ImageField(null=True)
    place_of_employment = models.CharField(max_length=255, null=True)
    about_yourself = models.TextField(null=True)
    location = models.CharField(max_length=255, null=True)
    rank1 = 'r1'
    rank2 = 'r2'
    rank3 = 'r3'
    RANK_CHOICES = [
        (rank1, 'Freshman'),
        (rank2, 'Middle'),
        (rank3, 'Experienced')
    ]
    status1 = 'status_none'
    status2 = 'status_educating'
    status3 = 'status_working'
    STATUS_CHOICES = [
        (status1, 'none'),
        (status2, 'educating'),
        (status3, 'working')
    ],
    rating = models.IntegerField(default=10)
    # access_token = models.TextField(null=True, blank=True)
