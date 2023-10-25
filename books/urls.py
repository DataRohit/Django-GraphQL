from django.urls import path

from graphene_django.views import GraphQLView

from books.schema import schema

urlpatterns = [
    path("", GraphQLView.as_view(graphiql=True, schema=schema), name="books__home"),
]
