# from django.urls import path
from rest_framework.routers import DefaultRouter

from question.views import QuestionViewSet, AnswerViewSet, CommentViewSet, RateViewSet, TagViewSet, SkillViewSet, \
    QuestionItemViewSet, QuestionCreateView

router = DefaultRouter()
router.register('api/answers', AnswerViewSet)
# router.register('api/answer/item', AnswerItemViewSet)


router.register('api/questions', QuestionViewSet)
router.register('api/question/item', QuestionItemViewSet)
router.register('api/question/create', QuestionCreateView)


router.register('api/comments', CommentViewSet)
router.register('api/rate', RateViewSet)
router.register('api/tag', TagViewSet)
router.register('api/skills', SkillViewSet)


urlpatterns = [
    # path('test', View.as_view())
]
urlpatterns += router.urls
