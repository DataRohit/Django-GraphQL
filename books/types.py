import graphene
from graphene_django import DjangoObjectType

from books.models import *


class BooksNode(DjangoObjectType):
    class Meta:
        model = Books
        fields = "__all__"
        filter_fields = {
            "category": ["icontains"],
        }
        interfaces = (graphene.relay.Node,)
