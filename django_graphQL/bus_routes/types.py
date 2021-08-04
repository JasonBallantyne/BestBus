from graphene_django import DjangoObjectType

from .models import *


class BusRouteType(DjangoObjectType):
    class Meta:
        model = BusRoute


class UniqueRoutesType(DjangoObjectType):
    class Meta:
        model = UniqueRoutes


class UniqueStopsType(DjangoObjectType):
    class Meta:
        model = UniqueStops
