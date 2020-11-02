from django.db import models
from django.contrib.auth.models import User
from task2.chatting.models import DateParent, Question


class UserProfile(User):
    avatar = models.ImageField(null=True)
    place_of_employment = models.CharField(max_length=255)
    about_yourself = models.TextField()
    location = models.CharField(max_length=255)
    rank1 = 'r1'
    rank2 = 'r2'
    rank3 = 'r3'
    RANK_CHOICES = (
        (rank1, 'Freshman'),
        (rank2, 'Middle'),
        (rank3, 'Experienced')
    )
    status1 = 'status_educating'
    status2 = 'status_working'
    STATUS_CHOICES = (
        (status1, 'educating'),
        (status2, 'working')
    )


class Tag(models.Model, DateParent):
    name = models.CharField(max_length=255)
    question_id = models.ManyToManyField(to=Question)


class Skill(models.Model):
    user_id = models.OneToOneField(to=UserProfile, on_delete=models.CASCADE)
    tag_id = models.ManyToManyField(to=Tag)
