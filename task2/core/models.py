from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

from task2.core.date import DateParent


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


class Question(models.Model, DateParent):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)


class Answer(models.Model, DateParent):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE)


# class Comment(MPTTModel):
#     text = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     user_id = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, null=True)
#     question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE, null=True)
#     answer_id = models.ForeignKey(to=Answer, on_delete=models.CASCADE, null=True)
#     comment_id = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


class Comment(MPTTModel, DateParent):
    text = models.TextField()
    # date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Tag(models.Model, DateParent):
    name = models.CharField(max_length=255)
    question_id = models.ManyToManyField(to=Question)
    # date_create = models.DateTimeField(auto_now_add=True)
    # date_update = models.DateTimeField()
    # user_id = models.ManyToManyField(to=UserProfile)


class Rate(models.Model):
    count = models.IntegerField(default=1)
    user_id = models.OneToOneField(to=UserProfile, on_delete=models.CASCADE)
    question_id = models.OneToOneField(to=Question, on_delete=models.CASCADE, null=True)
    answer_id = models.OneToOneField(to=Answer, on_delete=models.CASCADE, null=True)
    comment_id = models.OneToOneField(to=Comment, on_delete=models.CASCADE, null=True)


class Skill(models.Model):
    user_id = models.OneToOneField(to=UserProfile, on_delete=models.CASCADE)
    tag_id = models.ManyToManyField(to=Tag)
