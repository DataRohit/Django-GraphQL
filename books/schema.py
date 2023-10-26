import graphene
from graphene import ObjectType
from graphene_django.filter import DjangoFilterConnectionField

from books.types import *


class Query(ObjectType):
    book = graphene.relay.Node.Field(BooksNode)
    all_books = DjangoFilterConnectionField(BooksNode)


schema = graphene.Schema(query=Query)
