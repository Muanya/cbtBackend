from django.urls import path
from .views import QuestionView, ChoiceView

urlpatterns = [
    path('', QuestionView.as_view(), name='question_view'),
    path('choices/', ChoiceView.as_view(), name='choice_view'),
]
