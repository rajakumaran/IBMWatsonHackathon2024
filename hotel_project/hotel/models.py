from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Hotel(models.Model):
    app_label = 'hotel'  # Replace 'hotels' with the actual name of your app
    _id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    region_winter_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name

class Booking(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer_name} - {self.hotel.name}"

class Room(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    type = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    max_occupancy = models.IntegerField()

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number}"

class RoomAvailability(models.Model):
    _id = models.UUIDField(primary_key=True, editable=False)
    availability_id = models.UUIDField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    nights = models.IntegerField()
    zipcode = models.CharField(max_length=10)
    availability_date = models.DateField()

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room.room_number} - {self.availability_date}"