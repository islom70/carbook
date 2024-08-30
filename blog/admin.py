from django.contrib import admin

from blog.models import Car, Booking


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'year', 'price', 'color', 'is_available')
    search_fields = ('name', 'model', 'year', 'price', 'color', 'is_available')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car', 'start_time', 'end_time')
    search_fields = ('user', 'car', 'start_time', 'end_time')