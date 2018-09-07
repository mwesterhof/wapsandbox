from graphene_django import DjangoObjectType
import graphene

from .models import Person as PersonModel


class Person(DjangoObjectType):
    class Meta:
        model = PersonModel


class Query(graphene.ObjectType):
    users = graphene.List(Person)

    def resolve_users(self, info):
        return PersonModel.objects.all()


schema = graphene.Schema(query=Query)
