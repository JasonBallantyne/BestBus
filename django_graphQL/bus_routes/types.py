from graphene_django import DjangoObjectType

from .models import *


class UniqueRoutesType(DjangoObjectType):
    class Meta:
        model = UniqueRoutes


class UniqueStopsType(DjangoObjectType):
    class Meta:
        model = UniqueStops
