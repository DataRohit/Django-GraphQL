import graphene
from quiz.mutations import *

from graphene_django.filter import DjangoFilterConnectionField


class Query(graphene.ObjectType):
    category = graphene.relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    quiz = graphene.relay.Node.Field(QuizzesNode)
    all_quizzes = DjangoFilterConnectionField(QuizzesNode)

    question = graphene.relay.Node.Field(QuestionNode)
    all_questions = DjangoFilterConnectionField(QuestionNode)

    answer = graphene.relay.Node.Field(AnswerNode)
    all_answers = DjangoFilterConnectionField(AnswerNode)


class Mutation(graphene.ObjectType):
    add_category = AddCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
