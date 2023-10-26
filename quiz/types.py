import graphene

from quiz.models import *
from graphene_django import DjangoObjectType


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"
        filter_fields = {
            "id": ["exact"],
            "name": ["icontains"],
        }
        interfaces = (graphene.relay.Node,)


class QuizzesNode(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = "__all__"
        filter_fields = {
            "id": ["exact"],
            "title": ["icontains"],
            "category__name": ["icontains"],
        }
        interfaces = (graphene.relay.Node,)


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        fields = "__all__"
        filter_fields = {
            "id": ["exact"],
            "quiz__title": ["icontains"],
            "title": ["icontains"],
        }
        interfaces = (graphene.relay.Node,)


class AnswerNode(DjangoObjectType):
    class Meta:
        model = Answer
        fields = "__all__"
        filter_fields = {
            "id": ["exact"],
            "question__title": ["icontains"],
            "is_right": ["exact"],
        }
        interfaces = (graphene.relay.Node,)
