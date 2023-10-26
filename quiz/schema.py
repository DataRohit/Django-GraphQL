import graphene
from quiz.types import *

from django.db.models import Q


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType, id=graphene.String())
    all_quizzes = graphene.List(
        QuizzesType,
        id=graphene.String(),
        title=graphene.String(),
        category=graphene.String(),
    )
    all_questions = graphene.List(
        QuestionType, id=graphene.String(), title=graphene.String()
    )
    all_answers = graphene.List(
        AnswerType, id=graphene.String(), is_right=graphene.Boolean()
    )

    def resolve_all_categories(root, info, **kwargs):
        if kwargs:
            id = kwargs.get("id")
            return Category.objects.filter(id__exact=id)
        return Category.objects.all()

    def resolve_all_quizzes(root, info, **kwargs):
        if kwargs:
            id = kwargs.get("id")
            title = kwargs.get("title")
            category = kwargs.get("category")

            if id is not None:
                return Quizzes.objects.filter(id__exact=id)

            if title is not None:
                return Quizzes.objects.filter(title__icontains=title)

            if category is not None:
                return Quizzes.objects.filter(category__name__icontains=category)
        return Quizzes.objects.all()

    def resolve_all_questions(root, info, **kwargs):
        if kwargs:
            id = kwargs.get("id")
            title = kwargs.get("title")

            if id is not None:
                return Question.objects.filter(id__exact=id)

            if title is not None:
                return Question.objects.filter(title__icontains=title)
        return Question.objects.all()

    def resolve_all_answers(root, info, **kwargs):
        if kwargs:
            id = kwargs.get("id")
            is_right = kwargs.get("is_right")

            if id is not None:
                return Answer.objects.filter(id__exact=id)

            if is_right is not None:
                return Answer.objects.filter(is_right__exact=is_right)
        return Answer.objects.all()


schema = graphene.Schema(query=Query)
