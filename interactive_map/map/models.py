from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    def get_user_coordinates(self):
        return self.latitude, self.longitude
