import graphene
from graphene import ObjectType

from books.types import *


class Query(ObjectType):
    all_books = graphene.List(BooksType)

    def resolve_all_books(root, info):
        return Books.objects.all()


schema = graphene.Schema(query=Query)
