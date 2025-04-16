from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

# View to handle GET (list all menu items) and POST (create a new menu item)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()  # Get all menu items
    serializer_class = MenuSerializer  # Use the MenuSerializer to format the data
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

# View to handle GET (retrieve a single menu item), PUT (update a menu item), and DELETE (delete a menu item)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Get all menu items
    serializer_class = MenuSerializer  # Use the MenuSerializer to format the data
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

# BookingViewSet - Handles standard actions for Booking model (GET, POST, PUT, DELETE)
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Get all bookings
    serializer_class = BookingSerializer  # Use the BookingSerializer to format the data
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
# auth token eb81f5b6d0696d63f0b52401863620a725bd4c4b