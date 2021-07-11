import graphene
from graphene_django import DjangoObjectType
from .models import BusRoute


class BusRouteType(DjangoObjectType):
    class Meta:
        model = BusRoute
        fields = ('id',
                  'trip_id',
                  'shape_id',
                  'stop_id',
                  'stop_sequence',
                  'destination',
                  'stop_name',
                  'latitude',
                  'longitude',
                  'ainm',
                  'route_num',
                  'stop_num')


class Query(graphene.ObjectType):
    all_bus_routes = graphene.List(BusRouteType)
    route_by_num = graphene.List(BusRouteType, route_num=graphene.String(required=True))
    route_by_stop = graphene.List(BusRouteType, stop_num=graphene.String(required=True))

    # returns a list of bus_route objects that have a matching route number
    def resolve_route_by_num(root, info, route_num):
        return_list = []
        for route in BusRoute.objects.all():
            if route.route_num == route_num:
                return_list.append(route)
        return return_list

    # returns a list of bus_route objects that have a matching stop number
    def resolve_route_by_stop(root, info, stop_num):
        return_list = []
        for route in BusRoute.objects.all():
            if route.stop_num == stop_num:
                return_list.append(route)
        return return_list

    def resolve_all_bus_routes(root, info):
        return BusRoute.objects.all()


schema = graphene.Schema(query=Query)
