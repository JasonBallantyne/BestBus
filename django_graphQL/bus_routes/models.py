from django.db import models


class BusRoute(models.Model):
    id = models.CharField("id", max_length=100, primary_key=True)
    trip_id = models.CharField("trip_id", max_length=100, default=0)
    shape_id = models.CharField("shape_id", max_length=100, default=0)
    stop_id = models.CharField("stop_id", max_length=50)
    stop_sequence = models.IntegerField("stop_sequence")
    destination = models.CharField("destination", max_length=100)
    stop_name = models.CharField("stop_name", max_length=100)
    latitude = models.FloatField("latitude")
    longitude = models.FloatField("longitude")
    ainm = models.CharField("ainm", max_length=100)
    route_num = models.CharField("route_num", max_length=20)
    stop_num = models.CharField("stop_num", max_length=20, default=0)

    def __str__(self):
        return self.id
