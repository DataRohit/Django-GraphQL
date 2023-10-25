from graphene_django import DjangoObjectType

from books.models import *


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = "__all__"
