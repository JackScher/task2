from django.contrib import admin

from question.models import Question, Answer, Rate, Skill, Tag

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Rate)
admin.site.register(Tag)
admin.site.register(Skill)
