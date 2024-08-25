from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hotel, Booking, Room, RoomAvailability
from .serializers import HotelSerializer, BookingSerializer, RoomSerializer, RoomAvailabilitySerializer
from django.urls import reverse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class HotelList(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingList(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomList(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomAvailabilityList(APIView):
    def get(self, request):
        availability = RoomAvailability.objects.all()
        serializer = RoomAvailabilitySerializer(availability, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RootView(APIView):
    renderer_classes = [JSONRenderer]
    
    def get(self, request):
        return Response({
            'hotels': request.build_absolute_uri(reverse('hotel-list')),
            'bookings': request.build_absolute_uri(reverse('booking-list')),
            'rooms': request.build_absolute_uri(reverse('room-list')),
            'room-availability': request.build_absolute_uri(reverse('room-availability-list')),
        })