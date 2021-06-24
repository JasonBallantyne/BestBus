import graphene
from graphene_django import DjangoObjectType
from .models import Customers


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customers
        fields = ('id', 'name', 'gender')


class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)

    def resolve_all_customers(root, info):
        return Customers.objects.all()


schema = graphene.Schema(query=Query)
