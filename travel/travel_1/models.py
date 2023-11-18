from django.db import models
class EuroTravel(models.Model):
    country = models.CharField(max_length=100)
    tour_cost = models.IntegerField()
    tour_description = models.TextField()

    hotel = models.CharField(max_length=100)
    hotel_description = models.TextField()
    transit = models.CharField(max_length=100)
    food = models.CharField(max_length=200)
    excursions = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} - {self.country} - {self.tour_cost} - {self.tour_description} - {self.hotel} - {self.hotel_description} - {self.transit} - {self.food} - {self.excursions}"