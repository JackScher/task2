from rest_framework.routers import DefaultRouter

from question.views import QuestionViewSet, AnswerCreateView, CommentViewSet, TagViewSet, SkillViewSet, \
    QuestionItemViewSet, QuestionCreateView

router = DefaultRouter()
router.register('api/answer/create', AnswerCreateView)


router.register('api/questions', QuestionViewSet)
router.register('api/question/item', QuestionItemViewSet)
router.register('api/question/create', QuestionCreateView)


router.register('api/comment/create', CommentViewSet)

# router.register('api/rate', RateViewSet)
router.register('api/tag', TagViewSet)
router.register('api/skills', SkillViewSet)


urlpatterns = [
    # path('test', View.as_view())
]
urlpatterns += router.urls
