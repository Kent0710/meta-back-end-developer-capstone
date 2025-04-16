"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views  # Import views from your restaurant app

# Create a router and register the BookingViewSet
router = DefaultRouter()
router.register(
    r"tables", views.BookingViewSet
)  # Register BookingViewSet with the 'booking' route
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('restaurant.urls')),
    path("admin/", admin.site.urls),
    path('restaurant/', include('restaurant.urls')),  # This includes all paths from restaurant.urls
    path("restaurant/menu/", include("restaurant.urls")),  # Menu routes
    path("restaurant/booking/", include(router.urls)),  # Booking routes from the router
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
