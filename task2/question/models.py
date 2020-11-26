from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class DateParent(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)                           #, format=settings.REST_FRAMEWORK['DATETIME_FORMAT']
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(DateParent):
    text = models.TextField()
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='comments')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Question(DateParent):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')
    comments = GenericRelation(Comment)


class Answer(DateParent):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='answers')
    comments = GenericRelation(Comment)


class Tag(DateParent):
    name = models.CharField(max_length=255)
    question_id = models.ManyToManyField(to=Question, related_name='tags', blank=True)


class Skill(models.Model):
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag_id = models.ManyToManyField(to=Tag)


class Vote(DateParent):
    voter = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='voter', default=1)
    # user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vote')
    # is_like = models.BooleanField(default=False)
    # is_dislike = models.BooleanField(default=False)
    action = models.CharField(max_length=255, default='up')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='vote')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
