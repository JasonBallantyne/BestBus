import graphene
from graphene_django import DjangoObjectType
from .models import Customers

'''The following classes and class methods are for providing 
graphene/GraphQL mutations.'''


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customers
        fields = ('id', 'name', 'gender')


class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)

    def resolve_all_customers(root, info):
        return Customers.objects.all()


class CreateCustomer(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    gender = graphene.String()

    class Arguments:
        name = graphene.String()
        gender = graphene.String()

    def mutate(self, info, name, gender):
        customer = Customers(name=name, gender=gender)
        customer.save()

        return CreateCustomer(
            id=customer.id,
            name=customer.name,
            gender=customer.gender
        )


class UpdateCustomer(graphene.Mutation):
    id = graphene.Int(required=True)
    name = graphene.String()
    gender = graphene.String()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        gender = graphene.String()

    def mutate(self, info, id, name, gender):
        customer = Customers(id=id, name=name, gender=gender)
        customer.save()

        return UpdateCustomer(
            id=customer.id,
            name=customer.name,
            gender=customer.gender
        )


# https://stackoverflow.com/questions/55442189/delete-mutation-in-django-graphql
class DeleteCustomer(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        customer = Customers(id=id)
        customer.delete()

        return DeleteCustomer(id=id)


class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    delete_customer = DeleteCustomer.Field()
    update_customer = UpdateCustomer.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
