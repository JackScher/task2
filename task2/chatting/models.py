from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


from task2.core.models import UserProfile


class DateParent:
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField()

    class Meta:
        abstract = True


class Question(models.Model, DateParent):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_id = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)


class Answer(models.Model, DateParent):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_id = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE)


class Comment(models.Model, DateParent):
    text = models.TextField()
    user_id = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Rate(models.Model):
    count = models.IntegerField(default=1)
    user_id = models.OneToOneField(to=UserProfile, on_delete=models.CASCADE)
    question_id = models.OneToOneField(to=Question, on_delete=models.CASCADE, null=True)
    answer_id = models.OneToOneField(to=Answer, on_delete=models.CASCADE, null=True)
    comment_id = models.OneToOneField(to=Comment, on_delete=models.CASCADE, null=True)
