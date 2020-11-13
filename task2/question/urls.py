from django.urls import path, include
from rest_framework.routers import DefaultRouter

from question.views import QuestionViewSet, AnswerViewSet, CommentViewSet, RateViewSet, TagViewSet, SkillViewSet

router = DefaultRouter()
router.register('api/questions', QuestionViewSet)
router.register('api/answers', AnswerViewSet)
router.register('api/comments', CommentViewSet)
router.register('api/rate', RateViewSet)
router.register('api/tag', TagViewSet)
router.register('api/skills', SkillViewSet)

urlpatterns = []
urlpatterns += router.urls
