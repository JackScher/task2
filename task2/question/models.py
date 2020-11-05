from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


from profiles.models import UserProfile


class DateParent:
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField()

    class Meta:
        abstract = True


class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Answer(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Rate(models.Model):
    count = models.IntegerField(default=1)
    user_id = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question_id = models.OneToOneField(to=Question, on_delete=models.CASCADE, null=True)
    answer_id = models.OneToOneField(to=Answer, on_delete=models.CASCADE, null=True)
    comment_id = models.OneToOneField(to=Comment, on_delete=models.CASCADE, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    question_id = models.ManyToManyField(to=Question)


class Skill(models.Model):
    user_id = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag_id = models.ManyToManyField(to=Tag)
