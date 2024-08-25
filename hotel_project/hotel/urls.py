from django.urls import path
from . import views

urlpatterns = [
    path('', views.RootView.as_view(), name='root'),
    path('hotels/', views.HotelList.as_view(), name='hotel-list'),
    path('bookings/', views.BookingList.as_view(), name='booking-list'),
    path('rooms/', views.RoomList.as_view(), name='room-list'),
    path('room-availability/', views.RoomAvailabilityList.as_view(), name='room-availability-list'),
]