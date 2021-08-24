from django.db import models


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
    line_id = models.CharField("line_id", max_length=10, default="None")
    names = models.TextField("names", default="None")
    gach_ainm = models.TextField("gach_ainm", default="None")
    stops = models.TextField("outbound_stops", default="None")
    latitudes = models.TextField("latitudes", default="None")
    longitudes = models.TextField("longitudes", default="None")
    destination = models.CharField("destination", max_length=50, default="None")
    ceann_scribe = models.CharField("ceann_scribe", max_length=50, default="None")
    direction = models.CharField("direction", max_length=50, default="None")
    first_departure_schedule = models.TextField("first_departure_schedule", default="None")

    def __str__(self):
        return self.id


class StopSequencing(models.Model):
    stop_num = models.CharField("id", max_length=10, default="None", primary_key=True)
    stop_route_data = models.TextField("stop_route_data", default="None")

    def __str__(self):
        return self.stop_num

