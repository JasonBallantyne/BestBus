from django.db import models


class BusRoute(models.Model):
    id = models.CharField("id", max_length=100, primary_key=True, default="None")
    trip_id = models.CharField("trip_id", max_length=100, default=0)
    shape_id = models.CharField("shape_id", max_length=100, default=0)
    stop_id = models.CharField("stop_id", max_length=50)
    stop_sequence = models.IntegerField("stop_sequence")
    destination = models.CharField("destination", max_length=100)
    stop_name = models.CharField("stop_name", max_length=100)
    latitude = models.FloatField("latitude")
    longitude = models.FloatField("longitude")
    ainm = models.CharField("ainm", max_length=100)
    route_num = models.CharField("self", max_length=50, default=0)
    stop_num = models.CharField("stop_num", max_length=20, default=0)
    direction = models.CharField("direction", max_length=50, default="None")

    def __str__(self):
        return self.id


class UniqueStops(models.Model):
    stop_id = models.CharField("id", max_length=50, primary_key=True)
    latitude = models.FloatField("latitude")
    longitude = models.FloatField("longitude")
    stop_name = models.CharField("stop_name", max_length=100)
    ainm = models.CharField("ainm", max_length=100)
    stop_num = models.CharField("stop_num", max_length=10, default="None")

    def __str__(self):
        return self.stop_id


class UniqueRoutes(models.Model):
    id = models.CharField("id", max_length=20, default="None", primary_key=True)
    route_num = models.CharField("route_num", max_length=10, default="None")
    names = models.TextField("names", default="None")
    gach_ainm = models.TextField("gach_ainm", default="None")
    stops = models.TextField("outbound_stops", default="None")
    latitudes = models.TextField("latitudes", default="None")
    longitudes = models.TextField("longitudes", default="None")
    destination = models.CharField("destination", max_length=50, default="None")
    direction = models.CharField("direction", max_length=50, default="None")

    def __str__(self):
        return self.id


