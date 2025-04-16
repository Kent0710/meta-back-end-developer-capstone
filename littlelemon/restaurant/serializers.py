from rest_framework import serializers
from .models import Menu, Booking  
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Specify the model
        fields = ['id', 'title', 'price', 'inventory']  # Fields to include in the serialized data

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify the model for Booking
        fields = '__all__'  # Include all fields from the Booking model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
