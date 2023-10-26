from quiz.models import *
from graphene_django import DjangoObjectType


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = "__all__"


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = "__all__"
