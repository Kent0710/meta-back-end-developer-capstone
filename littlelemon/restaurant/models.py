from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Custom validator for future date
def validate_future_date(value):
    if value <= timezone.now():
        raise ValidationError("Booking date must be in the future.")

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    booking_date = models.DateTimeField(validators=[validate_future_date])

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    inventory = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.title} : {str(self.price)}'