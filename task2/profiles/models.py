from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from question.models import Question, Tag


class UserProfile(AbstractUser):
    avatar = models.ImageField(null=True)
    place_of_employment = models.CharField(max_length=255, null=True)
    about_yourself = models.TextField(null=True)
    location = models.CharField(max_length=255, null=True)
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
    # access_token = models.TextField(null=True, blank=True)

#
# class Tag(models.Model):
#     name = models.CharField(max_length=255)
#     date_create = models.DateTimeField(auto_now_add=True)
#     date_update = models.DateTimeField()
#     question_id = models.ManyToManyField(to=Question)
#
#
# class Skill(models.Model):
#     user_id = models.OneToOneField(to=UserProfile, on_delete=models.CASCADE)
#     tag_id = models.ManyToManyField(to=Tag)
