from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views  

router = DefaultRouter()
router.register(
    r"tables", views.BookingViewSet
) 
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('restaurant.urls')),
    path("admin/", admin.site.urls),
    path('restaurant/', include('restaurant.urls')),  
    path("restaurant/menu/", include("restaurant.urls")), 
    path("restaurant/booking/", include(router.urls)),  
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
