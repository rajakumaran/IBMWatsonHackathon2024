from rest_framework import serializers
from .models import Hotel, Booking, Room, RoomAvailability

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['_id', 'name', 'address', 'city', 'state', 'zip_code', 'country', 'latitude', 'longitude', 'region_winter_rating']

class BookingSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['_id', 'hotel', 'customer_name', 'checkin_date', 'checkout_date', 'total_amount']

class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ['_id', 'hotel', 'room_number', 'type', 'price_per_night', 'availability', 'max_occupancy']

class RoomAvailabilitySerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = RoomAvailability
        fields = ['_id', 'availability_id', 'hotel', 'room', 'is_available', 'nights', 'zipcode', 'availability_date']