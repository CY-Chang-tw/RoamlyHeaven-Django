from django.db import models

class Host(models.Model):
    host_name = models.CharField(max_length=50, blank=True)
    host_email = models.EmailField(max_length=100)

class Listing(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):
    rate = models.FloatField(default=1)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Amenity(models.Model):
    listing = models.OneToOneField(Listing, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=50)
    bed = models.IntegerField(default=1)
    room_type = models.CharField(max_length=50)
    rules = models.CharField(max_length=500)

class Calendar(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    dateFrom = models.DateField()
    dateEnd = models.DateField()
    available = models.BooleanField()


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)