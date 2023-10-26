import graphene

from graphql_auth.schema import UserQuery, MeQuery

from users.mutations import AuthMutation


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
